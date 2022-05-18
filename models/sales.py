from odoo import models


class Sales_MO(models.Model):
    _inherit = 'sale.order'

    def mo_button(self):
        mrp = []
        for record in self.order_line:
            for bom_id in record.product_id.bom_ids:
                bom = record.env['mrp.bom'].search(
                    [('id', '=', bom_id.id)]).read()
                if bool(bom) == True:
                    mrp.append(record.product_id.id)
                    record.env['mrp.production'].create(
                        {'product_id': record.product_id.id,
                         'product_uom_id': record.product_id.bom_ids.product_uom_id.id,
                         'bom_id': bom_id.id,
                         'product_qty': record.product_uom_qty})

        mrp_prod_id = self.env['mrp.production'].search(
            [], limit=len(mrp), order='id desc')

        if len(mrp) == 1:
            return mrp_prod_id.get_formview_action()
        else:
            ids = [mrp_prod.id for mrp_prod in mrp_prod_id]
            return{
                'name': "Manufacturing Orders",
                'type': 'ir.actions.act_window',
                'res_model': 'mrp.production',
                'view_mode': 'tree',
                'target': 'current',
                'domain': [('id', 'in', ids)]
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
