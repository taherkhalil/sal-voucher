# -*- coding: utf-8 -*-
# Copyright (c) 2017, taher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.utils import today,getdate
import frappe
import string 
import random
from frappe.model.document import Document
from frappe.client import insert

class Vouchers(Document):
	def validate(self):
		size= 6
		chars= string.ascii_uppercase + string.digits
		self.code = ''.join(random.choice(chars) for _ in range(size))
		vc = frappe.new_doc("Voucher balance table")
		vc.code = self.code
		vc.remaining_amount = self.amount
		vc.insert(ignore_permissions=True)
		vc.save()
		



		acc = "Advances From Customer - DS"
		cash ="Cash - DS"
		je = frappe.new_doc("Journal Entry") #create jv to add advance
		je.posting_date = getdate()
		je.company = frappe.db.get_value("Company", frappe.db.get_value("Global Defaults", None, "default_company"), "company_name")
		je.bill_no = self.name
		je.reference_date = getdate()
		row1 = je.append("accounts", {})
		row1.account= acc
		row1.debit_in_account_currency = 0.0
		row1.credit_in_account_currency = self.amount

		row2 = je.append("accounts", {})
		row2.account = cash
	
		row2.debit_in_account_currency = self.amount
		row2.credit_in_account_currency = 0.0
		je.insert(ignore_permissions=True)
		je.submit()

def on_voucher_apply(doc,method):
	voucher_list =frappe.db.sql("select code from `tabVoucher balance table`",as_list=1)
	vl= [x[0] for x in voucher_list]
	frappe.errprint([voucher_list,vl])

	if doc.voucher != "0":
		frappe.errprint("not zero")
		if doc.voucher in vl:
			vou= frappe.get_doc("Voucher balance table", doc.voucher)
			balance= vou.remaining_amount
			if balance != 0:
				frappe.errprint("balance there")
				if doc.total >= vou.remaining_amount:
					doc.total =int(doc.total) - int(vou.remaining_amount)
					vou.remaining_amount = 0
					vou.save()
				else:
					frappe.errprint("voucher has more")
					doc.discount_amount = doc.total
					doc.total = 0
					doc.grand_total =0

					vou.remaining_amount = int(vou.remaining_amount) - int(doc.total)
					vou.insert()
					vou.save()
			else:
				frappe.msgprint("no Balance in voucher")
		else:
			frappe.msgprint("invalid voucher")



@frappe.whitelist()
def from_pos_call(code,total):
	frappe.errprint("in voucher")
	frappe.errprint(code)
	frappe.errprint(total)
	voucher_list =frappe.db.sql("select code from `tabVoucher balance table`",as_list=1)
	vl= [x[0] for x in voucher_list]
	frappe.errprint([voucher_list,vl])
	if code in vl:
		vou= frappe.get_doc("Voucher balance table", code)
		balance= vou.remaining_amount
		discount_amount =0
		frappe.errprint(discount_amount)
		if balance != 0:
			frappe.errprint("balance there")
			frappe.errprint(["flt-total",float(total),"total",total,"balance",balance,"rem",vou.remaining_amount])
			if total > balance:
				frappe.errprint("checking me greater")
			if float(total) >= float(vou.remaining_amount):
				frappe.errprint("total greater")
				discount_amount =float(vou.remaining_amount)
				vou.remaining_amount = 0
				vou.save()
				return discount_amount
			else:
				frappe.errprint("voucher has more")
				discount_amount = total
				vou.remaining_amount = float(vou.remaining_amount) - float(total)
				vou.save()
				return discount_amount

		else:
			frappe.msgprint("no Balance in voucher")



# def on_submit_jv(doc,method):
# 	frappe.errprint("called")
# 	frappe.errprint(doc.discount_amount)
# 	# global discount_amount
	
# 	if doc.voucher != 0:
# 		acc = "Advances From Customer - DS"
# 		sales ="Sales - DS"
# 		je = frappe.new_doc("Journal Entry") #create jv to add sales
# 		je.posting_date = getdate()
# 		je.company = frappe.db.get_value("Company", frappe.db.get_value("Global Defaults", None, "default_company"), "company_name")
# 		je.bill_no = doc.name
# 		# je.reference_name = doc.name
# 		je.reference_date = getdate()
# 		row1 = je.append("accounts", {})
# 		row1.account= acc
# 		row1.debit_in_account_currency = doc.discount_amount
# 		row1.credit_in_account_currency = 0.0

# 		row2 = je.append("accounts", {})
# 		row2.account = sales
# 		row2.debit_in_account_currency = 0.0
# 		row2.credit_in_account_currency = doc.discount_amount
# 		je.insert(ignore_permissions=True)
# 		frappe.errprint("jv created")
# 		je.submit()	




