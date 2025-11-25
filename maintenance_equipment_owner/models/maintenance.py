# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    is_external = fields.Boolean(
        default=False, help="Tick if it does not belong to the company"
    )
    owner_partner_id = fields.Many2one("res.partner", "Owner")
