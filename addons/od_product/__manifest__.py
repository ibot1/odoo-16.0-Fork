# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Extended Products & Pricelists',
    'author': 'Tobiloba Komolafe',
    'version': '1.2',
    'category': 'Sales/Sales',
    'depends': ['product'],
    'description': """
This is an extension of the base module for managing products and pricelists in Odoo.
========================================================================

It extends by containing functionalities for the field 'slug' and 'Additional barcode'.
    """,
    'data': [
        'views/product_views.xml'
    ],
    'installable': True,
    'license': 'LGPL-3',
}