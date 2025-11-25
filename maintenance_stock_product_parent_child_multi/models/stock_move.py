from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    product_id_domain = fields.Binary(compute="_compute_product_id_domain")

    @api.depends("picking_id")
    def _compute_product_id_domain(self):
        for move in self:
            domain = [("type", "=", "consu")]
            if move.picking_id.maintenance_equipment_id:
                product_ids = (
                    move.picking_id.maintenance_equipment_id.product_id.child_ids
                )
                move.product_id_domain = domain + [("id", "in", product_ids.ids)]
            else:
                move.product_id_domain = domain
