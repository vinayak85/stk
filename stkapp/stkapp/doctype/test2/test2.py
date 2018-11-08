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

@frappe.whitelist()
def auth():
	c = frappe.db.sql("""select api_key,api_secret,accesstoken from 1bd3e0294da19198.tabtest where name='b2550d9017';""", as_dict=1);
	frappe.msgprint(_(c[0].api_key));
	#return c[0].name;
	#dict = {'count': 0}
	#dict['count'] = c[0].name;
	#return dict;
	#frappe.msgprint(_(doc_name));
	#cnt=0;
	#frappe.msgprint(_(frappe.db.sql("""SELECT count(name) FROM tabSecondary where name like {0}""".format("'"+doc_name+"'"))))
	#for c in frappe.db.sql("""SELECT count(name) as name FROM tabSecondary where name like {0}""".format("'"+doc_name+"'")):
	#	frappe.msgprint(_(c[0]));
	
	#if(cnt > 0):
	
	#frappe.msgprint(_(cnt));


class test2(Document):
	pass

