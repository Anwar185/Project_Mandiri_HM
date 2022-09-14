from odoo import api, fields, models


class InputImunisasi(models.TransientModel):
    _name = 'posyandu.inputimunisasi'

    
    imunisasi_ids = fields.Many2many('posyandu.inputjenisimunisasi', string='Imunisasi',required=True)
    
    jumlah = fields.Integer(
        string='jumlah',
        required= False)


    def button_input_imunisasi(self):
        for rec in self:
            self.env['posyandu.inputjenisimunisasi'].search([('id', '=', rec.imunisasi_ids.id)]).write({'stok':rec.imunisasi_ids.stok + rec.jumlah})