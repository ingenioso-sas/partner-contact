from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    require_vat_for_sale = fields.Boolean(
        string='Requerir identificación del cliente para confirmar ventas o facturar',
        related='company_id.require_vat_for_sale',
        readonly=False,
    )


class ResCompany(models.Model):
    _inherit = 'res.company'

    require_vat_for_sale = fields.Boolean(
        string='Requerir identificación del cliente para confirmar ventas o facturar',
        default=False,
    )
