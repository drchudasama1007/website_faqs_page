# -*- coding: utf-8 -*-

from odoo import http, models, SUPERUSER_ID, fields, _
from odoo.http import request

class StaticContent(http.Controller):

    @http.route(["/faqs"], type='http', auth="public", website=True)
    def faqs_page(self, **kwargs):
        faqs = request.env['faq'].sudo().search([('is_published', '=', True)])
        return request.render('website_faqs_page.faqs_template', {'faqs': faqs})