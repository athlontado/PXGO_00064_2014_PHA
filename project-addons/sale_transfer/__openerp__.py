# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Pexego Sistemas Informáticos All Rights Reserved
#    $Jesús Ventosinos Mayor <jesus@pexego.es>$
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

{
    'name': "Sale transfer",
    'version': '1.0',
    'category': 'sale',
    'description': """Sale transfer""",
    'author': 'Pexego Sistemas Informáticos',
    'website': 'www.pexego.es',
    "depends" : ['base',
                 'sale',
                 'sale_stock',
                 'sale_commission',
                 'sale_pharma_group'],
    "init_xml": ['data/initialization.xml'],
    "data" : ['sale_view.xml',
              'settled_view.xml',
              'sale_workflow.xml',
              'templates/template_mail.xml',
             ],
    "installable": True
}
