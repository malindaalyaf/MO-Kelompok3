from odoo import models


class Sales_MO(models.Model):
    _inherit = 'sale.order'

    def mo_button(self):
        # mrp = []
        for record in self.order_line:
            for bom_id in record.product_id.bom_ids:
                bom = record.env['mrp.bom'].search([('id', '=', bom_id.id)]).read()
                if bool(bom) == True:
                    # mrp.append(product_id)
                    record.env['mrp.production'].create(
                        {'product_id': record.product_id.id, 
                        'product_uom_id': record.product_id.bom_ids.product_uom_id.id,
                        'bom_id': bom_id.id,  
                        'product_qty': record.product_uom_qty})
        return{
                    'type': 'ir.actions.act_window',
                    'res_model': 'mrp.production',
                    'view_mode': 'form',
                    }       

        # if len(mrp) == 1: 
        #     bom = self.product_id.get_formviewaction()
        # else:
        #     return{
        #             'name': "New",
        #             'type': 'ir.actions.act_window',
        #             'res_model': 'mrp.production',
        #             'view_mode': 'tree',
        #             }       