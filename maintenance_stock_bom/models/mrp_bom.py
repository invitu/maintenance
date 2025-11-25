from odoo import fields, models


class MrpBom(models.Model):
    _inherit = "mrp.bom"

    type = fields.Selection(
        selection_add=[("maintenance", "Maintenance")],
        ondelete={"maintenance": "set default"},
    )


class MrpBomLine(models.Model):
    _inherit = "mrp.bom.line"

    def _prepare_stock_move_values(self):
        """Give the values to create the corresponding picking line.

        :return: `stock.move` create values
        :rtype: dict
        """
        self.ensure_one()
        if self.bom_id.type != "maintenance":
            return
        vals = {
            "product_id": self.product_id.id,
            "product_uom_qty": self.product_qty,
            "product_uom": self.product_uom_id.id,
            "sequence": self.sequence,
            "name": self.product_id.partner_ref,
            "description_picking": self.product_id.display_name,
        }
        return vals
