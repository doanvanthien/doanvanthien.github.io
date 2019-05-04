# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json
import time
import random
import requests


class Zalo(models.Model):
    _name = 'zalo.zalo'

    name = fields.Char(string="Message", default="Hello friend, \n Nice to meet you.", required=1)
    partner_id = fields.Many2one('res.partner', string="Partner", required=1)
    user_id = fields.Char(string="User ID/Phone", related='partner_id.mobile', store=True)

    @api.onchange('name')
    def onchange_name(self):
        if self.name and self.partner_id.id:
            self.action_action()

    @api.multi
    def action_action(self):
        phone = self.user_id
        phone = list(phone)
        phone[0] = '84'
        phone = ''.join(phone)
        ZaloOaClient = self.env['zalo.oa.client'].create({
            'user_id': phone,
            'message': self.name
        })
        res = ZaloOaClient.action_get_oa_profile()
