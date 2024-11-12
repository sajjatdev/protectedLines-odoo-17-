# required cost field
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    standard_price = fields.Float(string='Cost', required=True)

    @api.constrains('standard_price')
    def _check_standard_price(self):
        for record in self:
            if record.standard_price is None or record.standard_price <= 0:  # or record.standard_price == 0.0:
                raise ValidationError("The Cost field cannot be zero or less than zero.")

