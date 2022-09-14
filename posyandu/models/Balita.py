from odoo import api, fields, models

class Balita(models.Model):
    _name = 'posyandu.balita'
    _description = 'New Description'

    name = fields.Char(string='Nama Balita')
    nik_balita= fields.Char(string='NIK')
    tgl=fields.Date(string='Tanggal Lahir')
    usia = fields.Char(string='Usia th')
    alamat=fields.Char(string='Alamat')
    berat_badan = fields.Char(string ='Berat Badan (kg)')
    tinggi_badan = fields.Char(string='Tinggi Badan (cm)')
    nama_ortu = fields.Char(string='Nama Orangtua')
    jenis_kelamin= fields.Selection([
        ('lk', 'Laki-Laki'), 
        ('pr', 'Perempuan'),
    ], string='Jenis Kelamin')
    dokter_ids = fields.Many2many('posyandu.dokter', string='Dokter')

