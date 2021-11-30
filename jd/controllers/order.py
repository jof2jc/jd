# -*- coding: utf-8 -*-
# Copyright (c) 2021, fardiansyah and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import requests
import json
from frappe.model.document import Document
from frappe.utils import logger, cstr, cint, convert_utc_to_user_timezone, now, flt, time_diff_in_hours, now_datetime, nowdate, getdate, get_weekdays, add_days, add_to_date, today, get_time, get_datetime
import datetime 
from frappe.desk.doctype.tag.tag import add_tag
from jd.controllers.jdapi import JdClient, JdRequest, get_jd_response, get_access_token_jd
from jd.controllers.jdauth import AuthClient, AuthRequest

from custom1.marketplace_flow.marketplace_integration import insert_new_sales_order


def run_get_marketplace_order_jd():
	if "is_marketplace_shop" not in frappe.db.get_table_columns("Customer"): return

	shop_list = frappe.get_list("Customer",fields=["name"],filters=[["marketplace_type","=","JDID"],["is_marketplace_shop","=",1],["api_key","!=",""], ["run_order_job","=","1"]])

	if not shop_list: return

	for shop in shop_list:
		print(shop.name, 'processing get_order_list JDID')
		access_token=""
		jd_doc = None
		api_doc = frappe.get_doc("Customer", shop.name)
		if api_doc:
			if api_doc.marketplace_type == "JDID": jd_doc = frappe.get_doc("Customer", shop.name)
			api_template = frappe.get_doc(api_doc.doctype,{"marketplace_type": api_doc.marketplace_type,"is_template":1})
			if api_template:
				api_doc.api_end_point = api_template.api_end_point

		if jd_doc:
			access_token = get_access_token_jd(jd_doc, commit_flag=True) or ""

		order_list = []
		result = {}
		order_detail_json = order_item_json = None
		if api_doc and api_doc.get("marketplace_type") and api_doc.get("api_end_point"):
			for r in api_doc.get("api_end_point",{"disabled":0,"type":("in",["Update Order Status","Get Order List","Get Order Detail"])}):
				if api_doc.marketplace_type == "JDID":

					if r.type == "Get Order List" and access_token:
						body={}
						header = r.header

						for k,v in json.loads(r.body.strip()).items():
							body.update({k:eval(v)})

							if k != "[page]":
								header = header.replace(k,cstr(body.get(k)))
						
						r.header = header.replace("[page]","1") #first time first page

						n=1
						while n >= 1:
							response = get_jd_response(r, api_doc, access_token)
							if response:
								if response.get("jingdong_seller_order_getOrderIdListByCondition_response"):
									result = response.get("jingdong_seller_order_getOrderIdListByCondition_response").get("result") or {}

									if result.get("model"):
										order_list += result.get("model") or []	#concat array list of orders	

										if len(result.get("model")) >= cint(body.get("[page_size]") or "100"): #continue api_call for next page
											n = 1 
											body["[page]"] += 1
											r.header = header.replace("[page]",cstr(body.get("[page]")))
										else: n = 0
									elif cint(result.get("code")) == 0: #failed
										n= 0
										frappe.log_error(cstr(result),title="%s: Error get_jd_response: %s" % (shop.name, r.type))
									else: n = 0
								else: n = 0
							else: n = 0	
							
						print(shop.name, 'order_list:', order_list)
						result={}

					elif r.type == "Get Order Detail" and order_list and access_token:
						for d in order_list:
							print(shop.name, "Get Order Detail:", d)

							response = get_jd_response(r, api_doc, access_token, d)
							
							if response:
								if response.get("jingdong_seller_order_getOrderInfoByOrderId_response"):
									result = response.get("jingdong_seller_order_getOrderInfoByOrderId_response").get("result")
									if result:
										order_data = result.get("model")
										order_items_data = order_data.get("orderSkuinfos")
										insert_new_sales_order(api_doc, order_data, order_items_data, r)
									elif cint(result.get("code"))==0 or not result.get("model"): #failed
										frappe.log_error(cstr(result),title="%s: Error get_jd_response: %s" % (shop.name, r.type))


