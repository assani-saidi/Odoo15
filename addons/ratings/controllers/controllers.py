# -*- coding: utf-8 -*-
# from odoo import http


# class Addons\ratings(http.Controller):
#     @http.route('/addons\ratings/addons\ratings', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons\ratings/addons\ratings/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons\ratings.listing', {
#             'root': '/addons\ratings/addons\ratings',
#             'objects': http.request.env['addons\ratings.addons\ratings'].search([]),
#         })

#     @http.route('/addons\ratings/addons\ratings/objects/<model("addons\ratings.addons\ratings"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons\ratings.object', {
#             'object': obj
#         })
