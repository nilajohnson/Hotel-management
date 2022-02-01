from odoo import fields, models, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError


class HotelModel(models.Model):
    _name = "accommodation.model"
    _rec_name = 'guesttt'
    _description = "accommodation_model"

# To add chatter
    _inherit = ['mail.thread']

    check_in_date = fields.Datetime(string='Check_in Date',
                                    default=datetime.now(),readonly = 1)
    check_out_date = fields.Datetime(string='Check_out Date',
                                     default=lambda self: fields.datetime.now()
                                     , readonly = 1)
    bed = fields.Selection(string='Bed',
                           selection=[('single', 'Single'),
                                      ('double', 'Double'),
                                      ('dormitory', 'Dormitory')])

    # series

    name = fields.Char(string="Sequence", readonly=True, required=True,
                       copy=False, default='New')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'hotel.service') or 'New'
        result = super(HotelModel, self).create(vals)
        return result
    # series__

    # room details fetching
    room = fields.Many2one('room.model')

    # guest name with address
    guesttt = fields.Many2one('res.partner', string='Guest')

    state = fields.Selection(string='status', default='draft',
                             selection=[('draft', 'Draft'),
                                        ('check in', 'Checked In'),
                                        ('check out', 'Checked Out'),
                                        ('cancel', 'Canceled')])

    # state change function
    def check_inn(self):
        self.state = 'check in'

    def check_outt(self):
        self.state = 'check out'

    def cancell(self):
        self.state = 'cancel'

    # expected date calculation
    expected_days = fields.Integer(string='Expected days')
    expected_date = fields.Datetime(string='Expected date')

    @api.onchange('expected_days')
    def onchange_next_date(self):
        if self. check_in_date:
            self.expected_date = self. check_in_date + timedelta(days=self.expected_days)

    address_proof = fields.Binary("Address")

    number_of_guests = fields.Integer(string='Number of Guests', required=True)
    tree_guest = fields.One2many('guestt.model','guestt_id')

    class GuestModel(models.Model):
        _name = "guestt.model"

        guestt_id = fields.Many2one('accommodation.model', string='Guest')
        namee = fields.Char(string='Name')
        gender = fields.Selection(string='Gender',
                             selection=[('female', 'Female'),
                                        ('male', 'Male')])
        age = fields.Integer()

    # validation of guest

    @api.constrains('number_of_guests','tree_guest')
    def _check_guest_details(self):
        print(len(self.tree_guest))
        if len(self.tree_guest) != self.number_of_guests:
             raise ValidationError("Please provide all guest details")

    # @api.multi
    # def _check_attachment_details(self):
    #     if ir_attachment.db_datas_fname == False :
    #         raise exceptions.UserError(("Please add attachment"))



