from odoo import models, fields

class NurserySaleOrder(models.Model):
    _inherit = "sale.order"

    flower = fields.Char(string="Nursery Flower")