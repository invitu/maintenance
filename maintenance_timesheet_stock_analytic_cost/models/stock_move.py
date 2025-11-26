
from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _prepare_analytic_lines(self):
        self.ensure_one()
        res = super()._prepare_analytic_lines()
        __import__('pdb').set_trace()
        return res

    def _prepare_analytic_line_values(self, account_field_values, amount, unit_amount):
        self.ensure_one()
        res = super()._prepare_analytic_line_values(account_field_values, amount, unit_amount)
        __import__('pdb').set_trace()
        return res
