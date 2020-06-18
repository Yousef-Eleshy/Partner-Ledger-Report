# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerLedgerCust(http.Controller):
#     @http.route('/partner_ledger_cust/partner_ledger_cust/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_ledger_cust/partner_ledger_cust/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_ledger_cust.listing', {
#             'root': '/partner_ledger_cust/partner_ledger_cust',
#             'objects': http.request.env['partner_ledger_cust.partner_ledger_cust'].search([]),
#         })

#     @http.route('/partner_ledger_cust/partner_ledger_cust/objects/<model("partner_ledger_cust.partner_ledger_cust"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_ledger_cust.object', {
#             'object': obj
#         })
