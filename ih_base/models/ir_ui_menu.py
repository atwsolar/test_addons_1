# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    def _load_menus_blacklist(self):
        res = super()._load_menus_blacklist()
        # if not self.env.user.has_group('base.group_system'):
        res.append(self.env.ref('mail.menu_root_discuss').id)
        res.append(self.env.ref('contacts.menu_contacts').id)
        res.append(self.env.ref('sale.sale_menu_root').id)
        res.append(self.env.ref('account.menu_finance').id)
        res.append(self.env.ref('project.menu_main_pm').id)
        res.append(self.env.ref('purchase.menu_purchase_root').id)
        res.append(self.env.ref('base.menu_board_root').id)
        res.append(self.env.ref('project.menu_project_management').id)
        
        return res