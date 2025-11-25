# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Maintenance Stock Bom",
    "summary": "Allows automatically stock picking from Bom",
    "author": "INVITU, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "version": "18.0.1.0.0",
    "category": "Warehouse",
    "website": "https://github.com/OCA/maintenance",
    "depends": [
        "maintenance_stock",
        "mrp",
    ],
    "data": [
        "views/stock_picking_views.xml",
    ],
    "installable": True,
}
