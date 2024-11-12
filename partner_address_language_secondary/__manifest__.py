# -*- coding: utf-8 -*-

{
    'name': 'Partner Name Translated',
    'version': '1.0',
    'summary': """Secondary language in the partner/customer/supplier form. Like address in arabic/Spanish/Chinese/Dutch/Greek/Russian/Hindi/French/Japanese/German/Portuguese/Korean/Italian/Turkish/Persian/Hebrew.  Translate/Translation """,
    'description': """Secondary language in the partner/customer/supplier form. Like address in arabic/Spanish/Chinese/Dutch/Greek/Russian/Hindi/French/Japanese/German/Portuguese/Korean/Italian/Turkish/Persian/Hebrew. Translate/Translation """,
    'category': 'Base',
    'author': 'bisolv',
    'website': "",
    'license': 'AGPL-3',

    'price': 0,
    'currency': 'USD',

    'depends': ['base_setup'],

    'data': [
        'views/res_config_settings_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
    ],
    'demo': [

    ],
    'images': ['static/description/banner.png'],
    'qweb': [],

    'installable': True,
    'auto_install': False,
    'application': False,
}
