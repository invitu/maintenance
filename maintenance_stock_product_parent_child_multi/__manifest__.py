# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Maintenance Stock Product Parent Child Multi",
    "summary": "Glue module between maintenance_stock and\
    product_parent_child_multi modules",
    "author": "INVITU, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "version": "18.0.1.0.0",
    "category": "Warehouse",
    "website": "https://github.com/OCA/maintenance",
    "depends": [
        "product_parent_child_multi",
        "maintenance_product",
        "maintenance_stock",
    ],
    "data": [
        "views/stock_picking_views.xml",
    ],
    "installable": True,
}
