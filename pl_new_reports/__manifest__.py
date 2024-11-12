{
    'name': 'Protected Lines PDF Reports',
    'summary': 'Protected Lines PDF Reports',
    'description': """ Protected Lines PDF Reports """,
    'license': 'LGPL-3',
    'author': 'Mo Compiler',
    'depends': ['sale', 'partner_address_language_secondary', 'lots_serials_in_invoice_lines'],
    'data': [
        "views/res_company_view.xml",
        "views/inherit_boxed_layout.xml",
        "views/inherit_sale_order_view.xml",
        "views/inherit_product_template_view.xml",
        "views/inherit_invoice_report.xml",
    ],
    'assets': {
        'web.report_assets_common': [
            'pl_new_reports/static/src/css/report_border.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'version': '1.0.0',
}
