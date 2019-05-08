# -*- coding: utf-8 -*-
from odoo import http

# class /opt/odoo/pruebas(http.Controller):
#     @http.route('//opt/odoo/pruebas//opt/odoo/pruebas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo/pruebas//opt/odoo/pruebas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo/pruebas.listing', {
#             'root': '//opt/odoo/pruebas//opt/odoo/pruebas',
#             'objects': http.request.env['/opt/odoo/pruebas./opt/odoo/pruebas'].search([]),
#         })

#     @http.route('//opt/odoo/pruebas//opt/odoo/pruebas/objects/<model("/opt/odoo/pruebas./opt/odoo/pruebas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo/pruebas.object', {
#             'object': obj
#         })