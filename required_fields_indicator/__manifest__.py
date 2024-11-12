# -*- coding: utf-8 -*-
{
    'name': "Required Fields Indicator",

    'summary': "Indicate all required fields in odoo",

    'description': """
               Indicate all required fields in odoo standard like odoo previous version.
    """,
    'author': "Hari",
    'category': 'Extra Rights',
    'version': '17.0.0.0',
    'depends': ['base', 'web'],
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'required_fields_indicator/static/scss/fields.scss',
        ],
    },
    'license': 'LGPL-3',
    'data': [],
    'demo': [],
}
