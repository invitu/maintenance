# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    next_request_date = fields.Datetime(
        compute="_compute_next_request_date",
        store=True,
    )

    @api.depends("maintenance_ids.schedule_date",
                 "maintenance_ids.stage_id",
                 "maintenance_ids.archive",
                 )
    def _compute_next_request_date(self):
        for equipment in self:
            next_request = equipment.maintenance_ids.search(
                [
                    ("equipment_id", "=", equipment.id),
                    ("schedule_date", "!=", False),
                    ("stage_id.done", "=", False),
                    ("archive", "=", False),
                ],
                order="schedule_date asc",
                limit=1,
            )
            equipment.next_request_date = next_request.schedule_date or ''
