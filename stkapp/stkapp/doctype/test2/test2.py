# -*- coding: utf-8 -*-
# Copyright (c) 2018, vin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import subprocess
from frappe import msgprint, _ 
import frappe.utils
from frappe.utils import cstr, flt, getdate, cint
from frappe.model.naming import make_autoname
from frappe import _
from frappe.model.mapper import get_mapped_doc
from upstox_api.api import *

@frappe.whitelist()
def auth():
	c = frappe.db.sql("""select api_key,api_secret,accesstoken,code from 1bd3e0294da19198.tabtest where name='b2550d9017';""", as_dict=1);
	key=c[0].api_key;
	secret=c[0].api_secret;
	access_token=c[0].api_secret;
	code==c[0].code;
	if code is None :
		s = Session(key);
		s.set_redirect_uri('http://upstox.com:3000');
		s.set_api_secret(secret);
		#print('URL: %s\n' % s.get_login_url())
		frappe.msgprint(_('URL: %s\n' % s.get_login_url()));
		
		
	
	if code is not None and access_token is None :
		s = Session(key);
		s.set_redirect_uri('http://upstox.com:3000');
		s.set_api_secret(secret);
		code==c[0].code;
		access_token = s.retrieve_access_token()
		frappe.msgprint(_('access_token: %s\n' % access_token));
		
			
	
	if code is not None and access_token is not None :
		try:
			u = Upstox(stored_api_key, stored_access_token);
			logged_in = True
			profile();
		except requests.HTTPError as e:
			frappe.msgprint(_('Sorry, there was an error [%s]. Let''s start over\n\n' % e));
			#print('Sorry, there was an error [%s]. Let''s start over\n\n' % e)
			return	
	
	

@frappe.whitelist()
def auth2():
	c = frappe.db.sql("""select api_key,api_secret,accesstoken,code from 1bd3e0294da19198.tabtest where name='b2550d9017';""", as_dict=1);
	key=c[0].api_key;
	secret=c[0].api_secret;
	access_token=c[0].api_secret;
	code==c[0].code;
	if access_token is None :
		s = Session(key);
		s.set_redirect_uri('http://upstox.com:3000');
		s.set_api_secret(secret);
		s.set_code(code)
		try:
			access_token = s.retrieve_access_token()
		except SystemError as se:
			frappe.msgprint(_('Uh oh, there seems to be something wrong. Error: [%s]' % se));
			return
			#print('Uh oh, there seems to be something wrong. Error: [%s]' % se)
            
		
	
	if access_token is not None :
		u = Upstox(stored_api_key, stored_access_token);
		logged_in = True

def profile():
	profile = u.get_profile();
	frappe.msgprint(_(profile));
class test2(Document):
	pass

