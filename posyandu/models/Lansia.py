from odoo import api, fields, models


class Lansia(models.Model):
    _name = 'posyandu.lansia'
    _description = 'New Description'
    
    name = fields.Char(string='Nama')
    nik_lansia = fields.Char('NIK')
    tgl_lansia = fields.Date(
        string='Tanggal Lahir')
    usia = fields.Char('Usia')
    alamat = fields.Char('Alamat')
    dokter_ids = fields.Many2many('posyandu.dokter', string='Dokter')