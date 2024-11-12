# pl_new_fields/models/sale_order_line.py

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.constrains('product_id', 'price_unit')
    def _check_price_unit(self):
        for line in self:
            if line.product_id and line.price_unit < line.product_id.mini_price:
                raise ValidationError((
                    'The unit price for product "%s" cannot be less than the minimum price of %.2f.'
                ) % (line.product_id.name, line.product_id.mini_price))
