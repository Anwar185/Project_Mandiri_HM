from odoo import api, fields, models

class InputJenisImunisasi(models.Model):
    _name = 'posyandu.inputjenisimunisasi'
    _description = 'New Description'

    name = fields.Selection([
        ('hepatitis_b', 'Imunisasi Hepatitis B'),
        ('polio', 'Imunisasi Polio'),
        ('bcg', 'Imunisasi BCG'),
        ('campak', 'Imunisasi Campak Rubella'),
        ('dpt', 'Imunisasi DPT-HB-HIB'),
        ('vaksin', 'Vaksin'),
    ], string='Nama Imunisasi')

    kode_imunisasi = fields.Char(string='Kode Imunisasi')
    stok = fields.Integer(string='stok')

    @api.onchange('name')
    def _onchange_kode_imunisasi(self):
        if self.name == 'hepatitis_b':
            self.kode_imunisasi ='IMN001' 
        elif self.name == 'polio':
            self.kode_imunisasi = 'IMN002' 
        elif self.name == 'bcg':
            self.kode_imunisasi = 'IMN003'
        elif self.name == 'campak':
            self.kode_imunisasi = 'IMN004'
        elif self.name == 'dpt':
            self.kode_imunisasi = 'IMN005'
        elif self.name == 'vaksin':
            self.kode_imunisasi = 'IMN006'

    imun_remaja = fields.Selection([
        ('vaksinhpv', 'Vaksin HPV'),
        ('vaksininf', 'Vaksin Influenza'),
        ('vaksintdap', 'Vaksin Tdap'),
    ], string='Nama Imunisasi')

    kode_imunisasi2 = fields.Char(string='Kode Imunisasi')

    @api.onchange('imun_remaja')
    def _onchange_kode_imunisasi2 (self):
        if self.imun_remaja == 'vaksinhpv':
            self.kode_imunisasi2 ='IMN011' 
        elif self.imun_remaja == 'vaksininf':
            self.kode_imunisasi2  = 'IMN012' 
        elif self.imun_remaja == 'vaksintdap':
            self.kode_imunisasi2 = 'IMN013'

    stok2 = fields.Integer(string='stok')
    
  
