# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    mrp_bom_id = fields.Many2one(
        comodel_name="mrp.bom",
        domain=[("type", "=", "maintenance")],
        # TODO add context to filter on the product
        # self.maintenance_equipment_id.product_id.mrp_bom_ids
    )

    @api.onchange("mrp_bom_id")
    def _onchange_mrp_bom_id(self):
        if not self.mrp_bom_id:
            return
        if self.maintenance_request_id:
            picking_lines_data = [fields.Command.clear()]
            picking_lines_data += [
                fields.Command.create(line._prepare_stock_move_values())
                for line in self.mrp_bom_id.bom_line_ids
            ]
            # set first line to sequence -99,
            # so a resequence on first page doesn't cause following page
            # lines (that all have sequence 10 by default)
            # to get mixed in the first page
            if len(picking_lines_data) >= 2:
                picking_lines_data[1][2]["sequence"] = -99

            self.move_ids_without_package = picking_lines_data
            self.scheduled_date = fields.Datetime.now() + relativedelta(
                days=(
                    self.mrp_bom_id.produce_delay + self.mrp_bom_id.days_to_prepare_mo
                )
            )
