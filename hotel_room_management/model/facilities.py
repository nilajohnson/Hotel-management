from odoo import fields, models


class HotelModel(models.Model):
    _name = "facilities.model"

    _description = "facilities_model"

    facilities = fields.Char(required=True)
