# pl_new_fields/models/mini_price.py

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    mini_price = fields.Float(string="Minimum Price",tracking=True)
