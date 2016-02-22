# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 Pharmadus. All Rights Reserved
#    $Óscar Salvador <oscar.salvador@pharmadus.com>$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, SUPERUSER_ID


class StockMove(models.Model):
    _inherit = 'stock.move'

    lot_str = fields.Char(string='Lots',
                          compute='_get_related_lots_str',
                          readonly=True,
                          store=True,
                          select=True)

    @api.depends('lot_ids')
    def _get_related_lots_str(self):
        for move in self:
            move.lot_str = u", ".join([x.name for x in move.lot_ids])

    def init(self, cr):
        move_ids = self.search(cr, SUPERUSER_ID, [('lot_str', 'in', (False, ''))])
        moves = self.browse(cr, SUPERUSER_ID, move_ids)
        moves._get_related_lots_str()


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    address_city = fields.Char(related='partner_id.city', store=True)
    address_zip = fields.Char(related='partner_id.zip', store=True)
    address_country = fields.Char(related='partner_id.country_id.name', store=True)
    picking_type_desc = fields.Char(compute='_compute_picking_type_desc')

    @api.one
    @api.depends('picking_type_id')
    def _compute_picking_type_desc(self):
        types = {'outgoing': ' - (Albarán de salida)',
                 'incoming': ' - (Albarán de entrada)',
                 'internal': ' - (Albarán interno)'}
        self.picking_type_desc = types.get(self.picking_type_id.code, '')