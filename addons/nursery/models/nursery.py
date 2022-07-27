from odoo import models, fields


class Flower(models.Model):
    _name = "nursery.flowers"
    _description = "model of flowers from the nursery we want to sell"

    name = fields.Char(required=True)
    species = fields.Char()
    price = fields.Float(required=True)
    growing_days = fields.Integer()
    seed_germination_date = fields.Date()