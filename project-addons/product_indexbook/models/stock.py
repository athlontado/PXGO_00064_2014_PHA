# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Pharmadus. All Rights Reserved
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
##############################################################################
#

from openerp import models, fields, api


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    @api.one
    def qc_check_if_need_pis(self, vals):
        # Check if destination location are affected by quality control,
        # product has P.I.S. and quant has lot assigned
        # If true and is not already created, create new
        # product identification sheet entry
        location_obj = self.env['stock.location']
        location = location_obj.browse([vals['location_id']]) if \
            vals.get('location_id') else self.location_id
        warehouse_id = location_obj.get_warehouse(location)
        warehouse = self.env['stock.warehouse'].browse(warehouse_id)
        product = self.env['product.template'].browse([vals['product_id']]) if \
            vals.get('product_id') else self.product_id
        lot = vals['lot_id'] if vals.get('lot_id') else self.lot_id.id
        qc_pis = self.env['qc.pis']
        if warehouse.wh_qc_stock_loc_id == location and \
                product.qc_has_pis and lot:
            # One P.I.S. for each lot
            if (qc_pis.search_count([('lot', '=', lot)]) == 0):
                qc_pis.create({'lot': lot, 'reference': product.id})

    @api.model
    def create(self, vals):
        self.qc_check_if_need_pis(vals)
        return super(StockQuant, self).create(vals)

    @api.multi
    def write(self, vals):
        for quant in self:
            quant.qc_check_if_need_pis(vals)
        return super(StockQuant, self).write(vals)
