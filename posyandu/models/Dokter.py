from odoo import api, fields, models


class Dokter(models.Model):
    _name = 'posyandu.dokter'
    _description = 'New Description'
    
    name = fields.Char(string='Nama')
    alamat = fields.Char('Alamat')
    image_dok = fields.Image('image_dok')
    id_dokter = fields.Char('id_dokter')
    dokter_spesialis = fields.Selection([
        ('dokter_balita', 'Dokter Balita'),
        ('dokter_ibu_hamil', 'Dokter Ibu Hamil'),
        ('dokter_remaja', 'Dokter Remaja'),
        ('dokter_lansia', 'Dokter Lansia'),
    ], string='dokter_spesialis')

    pasien_imunisasi = fields.Char(string='Nama Pasien')

    # @api.onchange('dokter_spesialis')
    # def _onchange_pasien_imunisasi(self):
    #     if self.dokter_spesialis == 'dokter_balita':
    #         self.pasien_imunisasi =''
    #     elif self.dokter_spesialis== 'dokter_ibu_hamil':
    #         self.pasien_imunisasi = ''
    #     elif self.dokter_spesialis== 'dokter_remaja':
    #         self.pasien_imunisasi = ''
    #     elif self.dokter_spesialis== 'dokter_lansia':
    #         self.pasien_imunisasi = ''
        
    sql_constraints = [
    (' id_dokter_unik', 'unique (id_dokter)', 'Nomor Nota tidak boleh sama!')]


