from odoo import api, fields, models


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    total_cost = fields.Float(
        string="Total cost",
        compute="_compute_equipment_total_cost", readonly=True, store=True
    )

    @api.depends("maintenance_ids.total_cost")
    def _compute_equipment_total_cost(self):
        for equipment in self:
            equipment.total_cost = sum(
                request.total_cost for request
                in equipment.maintenance_ids
            )

    def action_view_account_analytic_line_ids(self):
        """
        Access to the current timesheets for this maintenance request
        The view will be restricted to the current request and only HR managers
        could create timesheets for every employee
        """
        self.ensure_one()
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "maintenance_timesheet_stock_analytic_cost.total_costs_action_from_equipment"
        )
        action["domain"] = [("maintenance_request_id", "in", self.maintenance_ids)]
        action["context"] = {
            # "default_project_id": self.project_id.id,
            # "default_task_id": self.task_id.id,
            # "default_maintenance_equipment_id": self.id,
            "readonly_employee_id": not self.env.user.has_group(
                "hr_timesheet.group_timesheet_manager"
            ),
        }
        return action
