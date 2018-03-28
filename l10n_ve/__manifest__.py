# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2017 Engineer & Nano Group, C.A. (<http://www.eyngroup.com.ve>).

{	
	'name': 'Venezuela - Accounting',
    'version': '1.0',
    'category': 'Localization',
    'description': """  TEST 1.8.1 """,
    'author': 'Iron Graterol',
    'website': 'http://www.eyngroup.com.ve',
    'depends': ['account'],
    'data': [
        'data/l10n_ve_chart_data.xml',
        'data/account.account.template.csv',
        'data/account.chart.template.csv',
        'data/account.account.tag.csv',
        'data/account.tax_group_data.xml',		
        'data/account.tax.template.csv',
        'data/account.chart_template_data.yml',
	],
}