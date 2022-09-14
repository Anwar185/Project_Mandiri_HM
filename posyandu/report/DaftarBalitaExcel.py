from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.posyandu_report_balita_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()
    def generate_xlsx_report(self, workbook, data, balita):
        sheet = workbook.add_worksheet('Daftar Balita')
        bold = workbook.add_format({'bold': True})  
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'NIK')
        sheet.write(1, 1, 'Nama Balita')
        sheet.write(1, 2, 'Tanggal Lahir')
        sheet.write(1, 3, 'Usia')
        sheet.write(1, 4, 'Alamat')
        sheet.write(1, 5, 'Jenis Kelamin')
        sheet.write(1, 6, 'Nama Orang Tua')
        sheet.write(1, 7, 'Berat Badan')
        sheet.write(1, 8, 'Tinggi Badan')
        row = 1
        col = 0
        for obj in balita:
            report_name = obj.name
            col = 0
            row += 1
            sheet.write(row, col, obj.nik_balita)
            sheet.write(row, col+1, obj.name)
            sheet.write(row, col+2, obj.tgl)
            sheet.write(row, col+3, obj.usia)
            sheet.write(row, col+4, obj.alamat)
            sheet.write(row, col+5, obj.jenis_kelamin)
            sheet.write(row, col+6, obj.nama_ortu)
            sheet.write(row, col+7, obj.berat_badan)
            sheet.write(row, col+8, obj.tinggi_badan)