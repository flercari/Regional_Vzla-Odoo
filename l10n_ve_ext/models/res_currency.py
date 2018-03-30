# -*- coding: utf-8 -*-
from odoo import fields, models

class Currency(models.Model):
	_inherit = 'res.currency'
	
    name = fields.Char(symbol = 'Bs.')
	name = fields.Char(currency_unit_label = 'Bolivar')

'''
            <field name = "name" > VEF < /field >
            <field name = "symbol" > Bs. < /field >
            <field name = "rounding" > 0.01 < /field >
            <field name = "active" eval = "False"/>
            <field name = "currency_unit_label" > Bolivar < /field >
            <field name = "currency_subunit_label" > Centimos < /field >


class CountryState(models.Model):
    _inherit = 'res.country.state'

    l10n_in_tin = fields.Char('TIN Number', size=2, help="TIN number-first two digits")
	
'''