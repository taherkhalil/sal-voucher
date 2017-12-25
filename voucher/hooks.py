# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "voucher"
app_title = "Voucher"
app_publisher = "taher"
app_description = "Voucher for a perticular amount for anyone to use"
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "taherkhalil52@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/voucher/css/voucher.css"
# app_include_js = "/assets/voucher/js/voucher.js"

# include js, css files in header of web template
# web_include_css = "/assets/voucher/css/voucher.css"
# web_include_js = "/assets/voucher/js/voucher.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "voucher.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "voucher.install.before_install"
# after_install = "voucher.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "voucher.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	# "*": {
# 	# 	"on_update": "method",
# 	# 	"on_cancel": "method",
# 	# 	"on_trash": "method"
# 	# }
# 	"Sales Invoice" : {
# 		# "validate": "package.packages.doctype.packages.packages.package_buy",
# 		"on_submit": "voucher.voucher.doctype.vouchers.vouchers.on_submit_jv"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"voucher.tasks.all"
# 	],
# 	"daily": [
# 		"voucher.tasks.daily"
# 	],
# 	"hourly": [
# 		"voucher.tasks.hourly"
# 	],
# 	"weekly": [
# 		"voucher.tasks.weekly"
# 	]
# 	"monthly": [
# 		"voucher.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "voucher.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "voucher.event.get_events"
# }

