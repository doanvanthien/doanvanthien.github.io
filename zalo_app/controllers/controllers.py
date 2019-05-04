# -*- coding: utf-8 -*-
from odoo import http

class IziZalo(http.Controller):

    @http.route('/zalo_url/', auth='public')
    def call_url(self, **kw):
        print( "Hello, world")
        print("His")
        print(http)
        print(kw)
        zalo_config_id = http.request.env['zalo.config'].search([], limit=1)
        if len(zalo_config_id) == 1:
            zalo_config_id.access_token_oa = kw.get('access_token')

