from urllib.parse import urlparse
import jd
from jd.api.base import RestApi
import frappe, json
from jd.controllers.jdauth import AuthClient, AuthRequest
from frappe.utils import logger, cstr, cint, convert_utc_to_user_timezone, now, flt, time_diff_in_hours, now_datetime, nowdate, getdate, get_weekdays, add_days, add_to_date, today, get_time, get_datetime
import ast

class JdRequest(RestApi):
	def __init__(self, api , endpoint):
		parsed_uri = urlparse(endpoint)
		scheme = parsed_uri.scheme
		domain = parsed_uri.netloc
		port = 443 if scheme == "https" else 80
		self.ssl = True if port == 443 else False
		self.api_name = api
		
		RestApi.__init__(self, domain, port)

	def getapiname(self):
		return self.api_name

	def add_api_param(self, name, value):
		setattr(self, name, value)

	def get_response(self, access_token=None):
		return self.getResponse(access_token=access_token,ssl=self.ssl)

class JdClient(object):
	def __init__(self, key, secret):
		self.app_key = key
		self.app_secret = secret
		self.__setup_client()

	def __setup_client(self):
		jd.setDefaultAppInfo(self.app_key, self.app_secret)

	def execute(self,request, access_token=None):
		try:
			#print("access_token:", access_token)
			#print("JdClient execute >>>", request.__dict__)
			response = request.get_response(access_token=access_token) or {}
			print("JDClient Response", cstr(response))
			if cint(response.get("code"))!=0:
				frappe.log_error(cstr(request.__dict__) + "\n\n" + cstr(response),title="Error JDClient execute")

			return response

		except Exception as e:
			error_trace = frappe.get_traceback()
			if error_trace:
				frappe.log_error(cstr(request.__dict__) + "\n\n" + error_trace,title="Error JdClient execute")


def get_access_token_jd(api_doc,headers=None,body="", commit_flag=False, new_auth_code=""):
	access_token = ""
	for t in api_doc.get("api_end_point",{"disabled":0,"type":("in",["Refresh Token","Access Token"])}):
		if api_doc.marketplace_type == 'JDID' and t.type == "Refresh Token" and not new_auth_code:
			body={}
			hour_factor=0
			access_token = t.access_token or "" #use previous token first

			if t.body:
				body = ast.literal_eval(t.body) or {}
				if body.get("expires_in"):
					hour_factor = flt(body.get("expires_in")/3600.0)-4

			if hour_factor <=0: hour_factor = 20
			if (not t.last_token_created or not t.access_token) or (time_diff_in_hours(now_datetime(),t.last_token_created or t.modified) >= hour_factor):
				response = get_jd_response(t, api_doc) or {}
				
				if response.get("access_token"):
					#print("access_token: ", response.get("access_token"))
					access_token = cstr(response.get("access_token")) or ""
						
					if access_token:
						t.db_set("last_token_created",now_datetime())
						t.db_set("body",cstr(response))
						t.db_set("access_token", access_token)
						t.db_set("refresh_token", cstr(response.get("refresh_token")) or "")		
						if commit_flag: frappe.db.commit()	
		
		elif api_doc.marketplace_type == 'JDID' and t.type == "Access Token" and new_auth_code: #re-generate refresh token based on new authorization code
			t.authorization_code = new_auth_code
			response = get_jd_response(t, api_doc) or {}
			if response:
				if response.get("access_token"):
					print("new access_token_jd: ", response.get("access_token"))
					access_token = cstr(response.get("access_token")) or ""

				for r in api_doc.get("api_end_point",{"disabled":0,"type":("in",["Refresh Token"])}):
					if r.type == "Refresh Token" and access_token:
						r.db_set("authorization_code",new_auth_code)
						r.db_set("last_token_created",now_datetime())
						r.db_set("body",cstr(response))
						r.db_set("order_detail_json","")
						r.db_set("access_token", access_token)
						r.db_set("refresh_token", cstr(response.get("refresh_token")) or "")

						frappe.db.commit()

				return response

	return access_token or ""


def get_jd_response(t, api_doc, access_token='', d=None, item=None):
	r = t
	request, response, created_before = None, None, None

	headers = json.loads(r.header.strip())
	client = None
	request = None
	try:
		client = eval(headers.get("client"))
		request = eval(headers.get("request"))	
	except Exception as e:
		error_trace = frappe.get_traceback()
		if error_trace: 
			frappe.log_error(cstr(headers) + "\n\n" + error_trace,title="%s, %s: Error JD Headers" % (api_doc.name, t.type))


	for k,v in headers.items():
	 	if "param" in k: eval(v)
		#else: k = eval(v)

	if client and request:
		try:
			#print(vars(request))
			response = client.execute(request=request,access_token=access_token)
			#print(api_doc.name, "JdRequest execute >>>", cstr(response))
		except Exception as e:
			error_trace = frappe.get_traceback()
			if error_trace: 
				frappe.log_error(cstr(vars(request)) + "\n\n" + error_trace,title="%s, %s: Error get_jd_response" % (api_doc.name, t.type))

	return response

