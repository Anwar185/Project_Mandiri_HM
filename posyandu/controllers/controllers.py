# -*- coding: utf-8 -*-
# from odoo import http


# class Posyandu(http.Controller):
#     @http.route('/posyandu/posyandu', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/posyandu/posyandu/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('posyandu.listing', {
#             'root': '/posyandu/posyandu',
#             'objects': http.request.env['posyandu.posyandu'].search([]),
#         })

#     @http.route('/posyandu/posyandu/objects/<model("posyandu.posyandu"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('posyandu.object', {
#             'object': obj
#         })
