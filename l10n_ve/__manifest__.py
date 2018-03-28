# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2017 Engineer & Nano Group, C.A. (<http://www.eyngroup.com.ve>).

{
    'name': 'Venezuela - Accounting',
    'version': '1.3',
    'category': 'Localization',
    'description': """
Venezuela Accounting Basic Module

General Chart of Accounts VEN-NIF.
Provide Templates for Chart of Accounts , Taxes, Regional Currencies, States""",
    'author': 'Iron Graterol',
    'website': 'http://www.eyngroup.com.ve',
    'depends': ['account','base_iban','base_vat'],
    'data': [
        'data/res_country_state_data.xml'
    ],
    'demo' : ['demo/l10n_ve_demo.xml']
}

'''
    'data': [
        'data/account_tax_group_data.csv',
        'data/account_account_tag_data.csv',
        'data/account_account_template_data.csv',
        'data/account_chart_template_data.csv',
        'data/account_chart_template_data.yml',
        'data/account_fiscal_position_template.data.csv',
        'data/account_tax_template_data.csv',
        'data/l10n.ve_chart_data.xml',
        'data/res_bank.csv',
        'data/res_country_state_data.xml',
        'data/res_currency_data.xml'
    ],
    '''