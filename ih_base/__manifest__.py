{
    "name": "Instalatur Hebat Base",
    "version": "1.0",
    "summary": "Instalatur Hebat Base",
    "author": "Instalatur Hebat",
    "depends": ["contacts", "sale_management", "purchase", "project"],
    "data": [
        'security/ir.model.access.csv',

        'data/dashboard_data.xml',

        'views/dashboard.xml',
        'views/purchase_order.xml',
        'views/project_view.xml',
        'views/sale_view.xml',
        'views/purchase_view.xml',
        'views/account_view.xml',
        'views/res_partner.xml',
    ],
    "assets": {
        'web.assets_backend': [
            'ih_base/static/src/scss/menu_dashboard.scss',
        ],
    },
    "installable": True,
}
