from odoo import models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            if order.company_id.require_vat_for_sale and not order.partner_id.vat:
                raise ValidationError(_(
                    "No es posible confirmar un pedido para un cliente sin NIT"
                    "o identificación cuando la opción Requerir identificación"
                    "del cliente está activa. Por favor, edita la ficha del"
                    "cliente para añadir la identificación correspondiente."
                    "Por favor, edite la ficha del cliente para añadirlo."
                ))
        return super(SaleOrder, self).action_confirm()
