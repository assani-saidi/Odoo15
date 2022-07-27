from odoo import api, fields, models


class CreateRemittanceWizard(models.TransientModel):
    _name = "create.remittance.wizard"

    wcif_rate = fields.Char(string="WCIF Rate", required=True)