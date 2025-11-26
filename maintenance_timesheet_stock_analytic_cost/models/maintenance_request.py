from odoo import api, fields, models


class MaintenanceRequest(models.Model):
    _inherit = "maintenance.request"

    total_cost = fields.Float(
        string="Total cost",
        compute="_compute_request_total_cost", readonly=True, store=True
    )

    @api.depends("timesheet_ids", "stock_picking_ids.state")
    def _compute_request_total_cost(self):
        for request in self:
            timesheet_cost = sum(line.amount for line in request.timesheet_ids)
            stock_cost = sum(line.amount for line in request.stock_picking_ids.move_ids.account_move_ids.line_ids.analytic_line_ids)
            request.total_cost = timesheet_cost + stock_cost

    def action_view_account_analytic_line_ids(self):
        """
        Access to the current timesheets for this maintenance request
        The view will be restricted to the current request and only HR managers
        could create timesheets for every employee
        """
        self.ensure_one()
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "maintenance_timesheet_stock_analytic_cost.total_costs_action_from_request"
        )
        action["domain"] = [("maintenance_request_id", "=", self.id)]
        action["context"] = {
            "default_project_id": self.project_id.id,
            "default_task_id": self.task_id.id,
            "default_maintenance_request_id": self.id,
            "readonly_employee_id": not self.env.user.has_group(
                "hr_timesheet.group_timesheet_manager"
            ),
        }
        return action
