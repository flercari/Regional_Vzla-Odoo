# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2017 Engineer & Nano Group, C.A. (<http://www.eyngroup.com.ve>).

{	
    'name': 'Venezuela - Accounting',
    'version': '2.0',
    'category': 'Localization',
    'description': """
Venezuela Accounting Module
===========================
General Chart of Accounts VEN-NIF.
Provide Templates for Chart of Accounts and Taxes""",
    'author': 'Iron Graterol',
    'website': 'http://www.eyngroup.com.ve',
    'depends': ['account'],
    'data': [
        'data/l10n_ve_chart_data.xml',
        'data/account.account.template.csv',
        'data/account.chart.template.csv',
        'data/account.account.tag.csv',
        'data/account.tax.group.csv',
        'data/account.tax.template.csv',
        'data/account_chart_template_data.yml',
	],
}