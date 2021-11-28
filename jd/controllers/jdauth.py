
from urllib.parse import urlparse
import requests
import frappe
from frappe.utils import cstr

class AuthRequest(object):
	def __init__(self, refresh_token=None , auth_code=None, endpoint=None):
		self.refresh_token = refresh_token
		self.auth_code = auth_code
		self.endpoint = endpoint
		self.grant_type = "refresh_token" if refresh_token else "authorization_code"

class AuthClient(object):
	def __init__(self, app_key, app_secret):
		self.app_key = app_key
		self.app_secret = app_secret

	def execute(self,request, access_token=None):
		url = None
		if request.grant_type == "refresh_token":
			url = f'{request.endpoint}?app_key={self.app_key}&app_secret={self.app_secret}&grant_type=refresh_token&refresh_token={request.refresh_token}'
		else:
			url = f'{request.endpoint}?app_key={self.app_key}&app_secret={self.app_secret}&grant_type=authorization_code&code={request.auth_code}'

		if url:
			try:
				print(url)
				response = requests.get(url=url)
				print(response.json())
				return response.json()
			except Exception as e:
				error_trace = frappe.get_traceback()
				if error_trace:
					print(error_trace)
					frappe.log_error(cstr(request.__dict__) + "\n\n" + error_trace,title="Error JD auth execute: %s" % request.grant_type)

