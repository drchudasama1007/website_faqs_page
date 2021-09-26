# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2021 Odoo Helper
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Website FAQs',
    'category': 'Website',
    'summary': "Website FAQs",

    'version': '13.0.1',
    'description': """
Website FAQs
==================
This module allows to create Dynamic Backend Configuration Quaestion and Answer For FAQs and Saperate Page For FAQs
        """,
    'author': 'Odoo Helper',
    'depends': ['base','website'],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/faqs_views.xml',
        'views/faqs.xml',
    ],
    'images': ['images/OdooHelper.jpg'],
    'price': 10.46,
    'currency': 'USD',

    'application': True,
    'installable': True,
    'auto_install': False,
}

