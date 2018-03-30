# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2017 Engineer & Nano Group, C.A. (<http://www.eyngroup.com.ve>).
{
    'name': 'Venezuela - Regional',
    'version': '1.2',
    'category': 'Localization',
    'description': """
Venezuela Module for Regional Parameters

Changes: Bs.F to Bs. , States , Banks """,
    'author': 'Iron Graterol',
    'website': 'http://www.eyngroup.com.ve',
    'depends': ['account', 'l10n_ve'],
    'data': [
        'data/res_currency_data.xml',
      	'data/res_country_state_data.xml',
      	'data/res.bank.csv',
    ],
}
