# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json
import requests
import time
import logging
import hashlib

_logger = logging.getLogger(__name__)


class ZaloConfig(models.Model):
    _name = 'zalo.config'

    name = fields.Char(string="Name", default='Name')
    app_id = fields.Char(string="Application ID", required=True)
    key_app_secret = fields.Char(string="Key Application Secret", required=True)
    oa_id = fields.Char(string="Official Account ID", required=True)
    key_oa_secret = fields.Char(string="Key Official Account Secret", required=True)
    default_oa_api_base = fields.Char(string="Default OA API Base", required=True,
                                      default='https://openapi.zalo.me/v2.0/oa')
    maximum_file_size = fields.Integer(string="MAXIMUM FILE SIZE", required=True, default=5242880)
    access_token_oa = fields.Char(string="Access Token OA")
    callback_url = fields.Char(string="Callback URL")

    @api.multi
    def action_get_access_token(self):
        self.ensure_one()
        link = 'https://oauth.zaloapp.com/v3/oa/permission?app_id=%s&redirect_uri=%s' %(self.app_id,self.callback_url)
        return {
            'type': 'ir.actions.act_url',
            'url': link,
            'target': 'new',
        }

class ZaloOaClient(models.TransientModel):
    _name = 'zalo.oa.client'

    name = fields.Char(string="Name")
    user_id = fields.Char(string='User')
    message = fields.Char(string="Message")

    def post(self, params):
        config = self.env['zalo.config'].search([], limit=1)
        if len(config) == 0:
            raise Exception("Please create a new Zalo Configuration ")
        endpoint = "%s=%s" % (config.default_oa_api_base, config.access_token_oa)
        timestamp = int(round(time.time() * 1000))
        oa_params = {
            'oaid': config.oa_id,
            'timestamp': timestamp,
        }
        params = {**params, **oa_params}
        return self.send_request(endpoint, params, 'POST')

    def send_request(self, endpoint, params, method):
        headers = {
            "Content-Type": "application/json"
        }

        if method == 'GET':
            response = requests.get(url=endpoint, params=params, headers=headers)
        elif method == 'POST':
            response = requests.post(url=endpoint, json=params, headers=headers)
        else:
            raise Exception("method is not supported")

        if response.status_code != 200:
            raise Exception(response.text + ' ' + response.status_code + ' ' + method)
        return response.json()

    def action_send_message(self):
        params = {
            "recipient": {'user_id': self.user_id},
            "message": {'text': self.message,
                        }
        }
        self.post(params)

    def action_get_oa_profile(self):
        config = self.env['zalo.config'].search([], limit=1)
        if len(config) == 0:
            raise Exception("Please create a new Zalo Configuration ")

        url_get_profile = 'https://openapi.zaloapp.com/oa/v1/getprofile'
        method = 'GET'
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        timestamp = int(round(time.time() * 1000))
        mac_str = config.oa_id + self.user_id + str(timestamp) + config.key_oa_secret
        mac_str = mac_str.encode('UTF-8')
        params = {
            "oaid": config.oa_id,
            "uid": self.user_id,
            "timestamp": timestamp,
            "mac": hashlib.sha256(mac_str).hexdigest()
        }
        res = self.send_request(url_get_profile, params, method)
        if 'data' in res.keys():
            data = res.get('data')
            if 'userIdByApp' in data.keys():
                userIdByApp = data.get('userIdByApp')
                params = {
                    "recipient": {'user_id': userIdByApp},
                    "message": {'text': self.message,
                                }
                }
                result = self.post(params)
                print(result)