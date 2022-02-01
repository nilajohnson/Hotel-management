from odoo import fields, models


class HotelModel(models.Model):
    _name = "guest.model"
    _rec_name = 'guest_name'
    _description = "guest_model"

    guest_name = fields.Char(required=True)
    guest_address = fields.Char(required=True)