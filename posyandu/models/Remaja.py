from odoo import api, fields, models


class Remaja(models.Model):
    _name = 'posyandu.remaja'
    _description = 'New Description'
    
    name = fields.Char(string='Nama')
    nik_remaja = fields.Char('NIK')
    tgl_remaja = fields.Date(
        string='Tanggal Lahir')
    usia = fields.Char('Usia')
    bb = fields.Char('Berat Badan')
    tb = fields.Char('Tinggi Badan')
    image = fields.Image('image')
    
    kesehatan= fields.Selection([
        ('sehat', 'Sehat'), 
        ('tidak', 'Tidak Sehat'),
    ], string='Kesehatan Tubuh')
    keluhan = fields.Char('keluhan')
    dokter_ids = fields.Many2many('posyandu.dokter', string='Dokter')

    