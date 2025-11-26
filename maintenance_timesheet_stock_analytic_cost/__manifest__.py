# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Maintenance Timesheet Total cost",
    "summary": "Adds total cost button on requests",
    "author": "INVITU, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "version": "18.0.1.0.0",
    "category": "Human Resources",
    "website": "https://github.com/OCA/maintenance",
    "depends": ["maintenance_timesheet", "maintenance_stock", "stock_analytic"],
    "data": [
        "views/maintenance_request_views.xml",
        "views/maintenance_equipment_views.xml",
    ],
    "installable": True,
}
