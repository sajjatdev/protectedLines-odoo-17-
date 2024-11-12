from odoo import api, fields, models


class resCompany(models.Model):
    _inherit = 'res.company'

    company_card = fields.Binary(string="Company Card", )
