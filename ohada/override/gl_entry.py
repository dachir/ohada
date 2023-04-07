import frappe
from erpnext.accounts.doctype.gl_entry.gl_entry import GLEntry
from erpnext.setup.utils import get_exchange_rate
    
class CustomGLEntry(GLEntry):

    def before_insert(self):
        #self.taux_reference = get_exchange_rate(self.account_currency,self.reference_currency,self.posting_date)
        pass

@frappe.whitelist()
def fix_exchange_rate():
    names = frappe.db.get_list('GL Entry', filters={'taux_reference': 0},fields=['name'], as_list=True)

    for name in names:
        gl_doc = frappe.get_doc('GL Entry',name[0])
        reference_currency = frappe.db.get_value('Company', gl_doc.company, 'reference_currency')
        taux_reference = get_exchange_rate(gl_doc.account_currency, reference_currency, gl_doc.posting_date)
        frappe.db.sql(
            """
            UPDATE `tabGL Entry` SET reference_currency = %s, taux_reference = %s
            WHERE name = %s
            """, (reference_currency,taux_reference, gl_doc.name)
        )