# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2017 Engineer & Nano Group, C.A. (<http://www.eyngroup.com.ve>).

{	
    'name': 'Venezuela - Regionalization',
    'version': '2.2',
    'category': 'Localization',
    'description': """
Venezuela Module for Regional Parameters
========================================
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
		'data/account.fiscal.position.template.csv',
        'data/account.fiscal.position.tax.template.csv',
        'data/account_chart_template_data.yml',
        'data/res_currency_data.xml',
      	'data/res_country_state_data.xml',
      	'data/res.bank.csv',
	],
}
