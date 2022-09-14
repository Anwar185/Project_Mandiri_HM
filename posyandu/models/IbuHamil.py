from odoo import api, fields, models


class IbuHamil(models.Model):
    _name = 'posyandu.ibuhamil'
    _description = 'New Description'

    nik_ibuhamil = fields.Char(string='NIK')
    name = fields.Char(string='Name')
    usia_kandungan = fields.Selection(
        string='Usia Kandungan',
        selection=[('1', '1 Bulan'), ('2', '2 Bulan'),('3', '3 Bulan'), ('4', '4 Bulan'), ('5', '5 Bulan'),
        ('6', '6 Bulan'), ('7', '7 Bulan'), ('8', '8 Bulan'), ('9', '9 Bulan')])
    tgl=fields.Date(string='Tanggal Lahir')
    alamat = fields.Char('Alamat')
    dokter_ids = fields.Many2many('posyandu.dokter', string='Dokter')