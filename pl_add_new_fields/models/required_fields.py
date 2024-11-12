from odoo import models, fields
# product.template
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    customer_taxes_id = fields.Many2many(
        'account.tax',
        'product_taxes_rel',
        'prod_id',
        'tax_id',
        string='Customer Taxes',
        required=True
    )

# res.partner
class ResPartner(models.Model):
    _inherit = 'res.partner'

    street = fields.Char(string='Street', required=True)
    phone = fields.Char(string='Phone', required=True)
    vat = fields.Char(string='VAT Number', required=True)
