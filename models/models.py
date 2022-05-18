# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sales_mo(models.Model):
#     _name = 'sales_mo.sales_mo'
#     _description = 'sales_mo.sales_mo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
