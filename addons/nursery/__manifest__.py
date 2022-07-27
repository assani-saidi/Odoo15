# -*- coding: utf-8 -*-
{
    'name': "nursery",

    'summary': "dev nursery containing flowers for sale",

    'description': """
        the application will allow users to store their flower type
        and to the holistic business process associated with it.
    """,

    'author': "Assani Saidi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'product', 'point_of_sale', "account", "om_hr_payroll", "hr"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/nursery_view.xml',
        'views/nursery_sale_view.xml',
        'reports/nursery_flower_report.xml',
        'reports/nursery_flower_report_template.xml',
        'views/templates.xml',
        'views/views.xml',
        'views/menus_view.xml',
        'views/label_report_template.xml',
        'views/receipt_sale_template.xml',
        'views/payroll_report_template.xml',
        'views/payroll_report_new.xml',
        'wizard/remittance_view.xml',
        'wizard/summary_view.xml'
        # 'static/src/xml/pos-print-extension.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
         'web.assets_qweb': [
            'nursery/static/src/xml/pos-print-extension.xml',
        ],
    }
}