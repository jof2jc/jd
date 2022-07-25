
from urllib.parse import urlparse
import requests
import frappe
from frappe.utils import cstr, cint

class AuthRequest(object):
	def __init__(self, refresh_token=None , auth_code=None, endpoint=None):
		self.refresh_token = refresh_token
		self.auth_code = auth_code
		self.endpoint = endpoint
		if refresh_token:
			self.grant_type = "refresh_token" 
		elif auth_code: 
			self.grant_type = "authorization_code"

class AuthClient(object):
	def __init__(self, app_key, app_secret):
		self.app_key = app_key
		self.app_secret = app_secret

	def execute(self,request, access_token=None):
		url = None
		if request.grant_type == "refresh_token":
			url = f'{request.endpoint}?app_key={self.app_key}&app_secret={self.app_secret}&grant_type=refresh_token&refresh_token={request.refresh_token}'
		elif request.grant_type == "authorization_code":
			url = f'{request.endpoint}?app_key={self.app_key}&app_secret={self.app_secret}&grant_type=authorization_code&code={request.auth_code}'

		if url:
			try:
				#print(url)
				response = requests.get(url=url) or {}
				print(response.json())
				response = response.json()
				if cint(response.get("code")):
					frappe.log_error(cstr(request.__dict__) + "\n\n" + cstr(url) + "\n\n" + cstr(response),title="Error JDAuth execute: %s" % request.grant_type)
				return response
			except Exception as e:
				error_trace = frappe.get_traceback()
				if error_trace:
					print(error_trace)
					frappe.log_error(cstr(request.__dict__) + "\n\n" + error_trace,title="Error JDAuth execute: %s" % request.grant_type)

