# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Venezuela - Accounting',
    'version': '1.0',
    'author': 'Eyngroup',
    'website': 'https://eyngroup/ven-nif',
    'category': 'Localization',
    'description': """
General Chart of Accounts VEN-NIF.
Provide Templates for Chart of Accounts , Taxes for Venezuela.""",
    'depends': [
        'account',
        'base_iban',
        'base_vat',
    ],
    'data': [
        'data/l10n_ve_chart_data.xml',
        'data/account.account.template.csv',
        'data/account.chart.template.csv',
        'data/account.account.tag.csv',
        'data/account.tax.group.csv',
        'data/account.tax.template.csv',
        'data/res.country.state.csv',
        'data/account_chart_template_data.yml',
    ],
    'demo' : ['demo/l10n_ve_demo.xml'],
}
