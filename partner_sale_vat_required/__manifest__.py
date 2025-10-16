{
    'name': 'Partner Sale VAT Required',
    'version': '13.0.1.0.0',
    'category': 'Sales',
    'summary': 'Require customer identification for sales orders.',
    'author': 'Ingenioso SAS',
    'website': 'https://www.ingenioso.com',
    'license': 'AGPL-3',
    'depends': [
        'sale_management',
    ],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
