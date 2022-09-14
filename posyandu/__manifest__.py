# -*- coding: utf-8 -*-
{
    'name': "posyandu",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizzard/inputimunisasi_wizzard_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/daftarimunisasi_view.xml',
        'views/form_ibu_hamil_view.xml',
        'views/form_input_data_balita.xml',
        'views/remaja_view.xml',
        'views/lansia_view.xml',
        'views/dokter_view.xml',
        'views/inputjenisimunisasi_view.xml',
        'report/report.xml',
        'report/print_data_balita_pdf.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
