# 版权（c）2023，Anzhi 和贡献者
# 有关许可信息，请参阅许可协议

#import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class PartQuoteRef(Document):
	def before_insert(self):
		exists = frappe.db.exists(
			"User Information",
			{
				"docstatus": DocStatus.submitted(),
			}
		)
		#if exists: