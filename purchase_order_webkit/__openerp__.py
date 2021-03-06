# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2011 Camptocamp SA (http://www.camptocamp.com)
#   @author Guewen Baconnier
#   Copyright (c) 2013 Ursa Information Systems (http://www.ursainfosystems.com)
#   @author Balaji Kannan
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

{
    'name': 'Purchase Order Report using Webkit Library',
    'version': '1.1',
    'category': 'Reports/Webkit',
    'description': """
Replaces the legacy rml Quotation / Purchase Order report by a brand new webkit report.
    """,
    'author': 'Camptocamp, Ursa Information Systems',
    'website': 'http://www.openerp.com, http://www.ursainfosystems.com',
    'depends': ['base', 'report_webkit', 'base_headers_webkit', 'purchase','ursa_group_lines'],
    'init_xml': [],
    'update_xml': ['purchase_report.xml'],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
}
