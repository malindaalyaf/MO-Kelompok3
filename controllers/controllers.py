# -*- coding: utf-8 -*-
# from odoo import http


# class SalesMo(http.Controller):
#     @http.route('/sales_mo/sales_mo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_mo/sales_mo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_mo.listing', {
#             'root': '/sales_mo/sales_mo',
#             'objects': http.request.env['sales_mo.sales_mo'].search([]),
#         })

#     @http.route('/sales_mo/sales_mo/objects/<model("sales_mo.sales_mo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_mo.object', {
#             'object': obj
#         })
