# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    maintenance_request_id = fields.Many2one(comodel_name="maintenance.request")

    @api.model_create_multi
    def create(self, vals_list):
        __import__('pdb').set_trace()
        maintenance_request_ids = [
            vals.get("maintenance_request_id")
            for vals in vals_list
            if vals.get("maintenance_request_id")
        ]
        self._check_request_done(maintenance_request_ids)
        return super().create(vals_list)
