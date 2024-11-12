from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    attention_id = fields.Many2one(comodel_name="res.partner", string="", domain="[('parent_id', '=', partner_id)]")
