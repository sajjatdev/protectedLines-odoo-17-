from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    source_order_id = fields.Many2one(comodel_name="sale.order", string="", compute="_compute_source_sale_order")

    @api.depends("line_ids.sale_line_ids")
    def _compute_source_sale_order(self):
        source_orders = self.line_ids.sale_line_ids.order_id
        if len(source_orders) > 1:
            self.source_order_id = False
        elif len(source_orders) == 1:
            self.source_order_id = source_orders.id
        else:
            self.source_order_id = False
