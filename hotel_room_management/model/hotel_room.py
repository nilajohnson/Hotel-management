from odoo import fields, models


class HotelModel(models.Model):
    _name = "room.model"
    _description = "ht_model"

    facilities = fields.Many2many('facilities.model')

    name = fields.Char(required=True)
    room_number = fields.Float(required=True)
    bed = fields.Selection(string='Bed',
                           selection=[('single', 'Single'), ('double', 'Double')
                               , ('dormitory', 'Dormitory')])

    field_name = fields.Many2many('res.partner', string="many2many_checkboxes")

    available_beds = fields.Float()
    # rent with currency
    price = fields.Monetary(string="Rent")
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda
                                      self: self.env.user.company_id.currency_id.id,
                                  required=True)


