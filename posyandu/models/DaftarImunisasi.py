from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class DaftarImunisasi(models.Model):
    _name = 'posyandu.daftarimunisasi'
    _description = 'Daftar'
    
    balita_id = fields.Many2one(comodel_name = 'posyandu.balita', string='Nama Balita', ondelete='cascade')
    
    imunisasi_id =fields.Many2one(
        string='imunisasi',
        comodel_name='posyandu.inputjenisimunisasi')
  
    tgl_imunisasi = fields.Date(
        string='Tanggal di Imunisasi',
        default=fields.Date.context_today,)

    kebutuhan = fields.Integer('Kebutuhan Imunisasi')

    detailimunisasi_ids = fields.One2many(
        comodel_name='posyandu.detailimunisasi',
        inverse_name='daftarimunisasi_id',
        string='Detail Imunisasi Ids')
    
    @api.constrains('kebutuhan')
    def _check_kebutuhan(self):
        for rec in self:
            if rec.kebutuhan <1:
                raise ValidationError('Silahkan Masukan Kebutuhan Imunisasi {} ..'. format(rec.imunisasi_id.name))
            elif (rec.imunisasi_id.stok < rec.kebutuhan):
                raise ValidationError('Stok {} tidak mencukupi, hanya tersedia {}'. format(rec.imunisasi_id.name,rec.imunisasi_id.stok))
    
    def write(self,vals):
        for rec in self:
            a = self.env ['posyandu.detailimunisasi'].search([('daftarimunisasi_id','=',rec.id)])
            print (a)
            for data in a :
                print(str(data.imunisasi_id.name)+' '+str(data.kebutuhan))
                data.imunisasi_id.stok += data.kebutuhan
        record = super (DaftarImunisasi,self).write(vals)
        for rec in self:
            b = self.env['posyandu.detailimunisasi'].search([('daftarimunisasi_id','=',rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.imunisasi_id.name)+' '+str(databaru.qty))
                    databaru.imunisasi_id.stok -= databaru.kebutuhan
                else :
                    pass
        return record

    @api.model
    def create(self, vals):
         line = super(DaftarImunisasi, self).create(vals)
         if line.kebutuhan:
             self.env['posyandu.inputjenisimunisasi'].search(
                [('id', '=', line.imunisasi_id.id)]
             ).write({'stok': line.imunisasi_id.stok - line.kebutuhan})
             return line
    # @api.unlink
    # def unlink(self):
    # if self.detailimunisasi_ids:
    #     daftarimunisasi= []
    #     for line in self:
    #         daftarimunisasi = self.env['posyandu.detailimunisasi'].search(
    #             [('imunisasi_id', '=', line.id)])
    #         print(daftarimunisasi)

    #     for ob in penjualan:
    #         print(ob.imunisasi_id.name + ' ' + str(ob.kebutuhan))
    #         ob.imunisasi_id.stok += ob.kebutuhan
    # line = super(DaftarImunisasi, self).unlink()

class DetailImumisasi(models.Model):
    _name = 'posyandu.detailimunisasi'
    _description = 'Detail'

    name = fields.Char(string='Nama')

    daftarimunisasi_id = fields.Many2one(
        comodel_name='posyandu.daftarimunisasi',
        string='Detail Imunisasi')

    

   