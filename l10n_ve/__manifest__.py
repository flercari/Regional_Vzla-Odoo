# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2017 Engineer & Nano Group, C.A. (<http://www.eyngroup.com.ve>).

{	
    'name': 'Venezuela - Accounting',
    'version': '1.0',
    'category': 'Localization',
    'description': """
Venezuela Accounting Basic Module

General Chart of Accounts VEN-NIF.
Provide Templates for Chart of Accounts, Taxes, Regional Currencies, States, List Bank""",
    'author': 'Iron Graterol',
    'website': 'http://www.eyngroup.com.ve',
    'depends': ['account'],
    'data': [
        'data/l10n_ve_chart_data.xml',
		'data/res_country_state_data.xml',
		'data/res.bank.csv',
        'data/account.account.template.csv',
        'data/account.chart.template.csv',
        'data/account.account.tag.csv',
        'data/account.tax.group.csv',
        'data/account.tax.template.csv',
        'data/account_chart_template_data.yml',
	],
}