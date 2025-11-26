
from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def _prepare_analytic_lines(self):
        res = super()._prepare_analytic_lines()
        request = self.move_id.stock_move_id.maintenance_request_id.id
        for dict in res:
            dict.update({'maintenance_request_id': request})
        return res
