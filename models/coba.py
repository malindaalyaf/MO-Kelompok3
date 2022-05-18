# from odoo import models


# class Inherit_Sale(models.Model):
#     _inherit = 'sale.order'

#     def button_action(self):
#         for record in self.order_line:
#             for bom_id in record.product_id.bom_ids:
#                 data = record.env['mrp.bom'].search([('id', '=', bom_id.id)]).read()
#                 if bool(data) == True:
#                     record.env['mrp.production'].create({
#                         'product_id': record.product_id.id, 
#                         'product_uom_id': record.product_id.bom_ids.product_uom_id.id, 
#                         'bom_id': bom_id.id, 
#                         'product_qty': record.product_uom_qty})