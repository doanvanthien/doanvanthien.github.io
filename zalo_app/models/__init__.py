# -*- coding: utf-8 -*-
from . import zalo_config
from . import zalo

#
# def create_oa_params(self, data):
#     timestamp = int(round(time.time() * 1000))
#
#     mac_content = ''
#     for key, value in data.items():
#         if type(value) is dict:
#             data[key] = json.dumps(value)
#         mac_content = data[key]
#
#     params = {
#         'oaid': oa_id,
#         'timestamp': timestamp,
#         # 'mac': MacUtils.build_mac(oa_info.oa_id, mac_content, timestamp, oa_info.secret_key)
#     }
#
#     params.update(data)
#     return params
#
#
# def post(self, url, data, access_token):
#     endpoint = "%s/%s?access_token=%s" % (DEFAULT_OA_API_BASE, url, access_token)
#     params = self.create_oa_params(data)
#     return self.send_request(endpoint, params, 'POST')
#
#
# def send_request(self, endpoint, params, method):
#     headers = {
#         'content-type': 'application/x-www-form-urlencoded',
#     }
#     headers.update(DEFAULT_HEADER)
#
#     headers = {
#         "Content-Type": "application/json"
#     }
#     x = random.randint(0, 3)
#     user_id = '3793926606656310526'
#
#     params = {
#         "recipient": {'user_id': user_id},
#         # "recipient": {'user_id': '0986861633'},
#         "message": {'text': self.name,
#                     }
#     }
#
#     if method == 'GET':
#         response = requests.get(url=endpoint, params=params, headers=headers)
#     elif method == 'POST':
#         # response = requests.post(url=endpoint, data=params.dumps(), headers=headers)
#         response = requests.post(url=endpoint, json=params, headers=headers)
#     else:
#         raise Exception("method is not supported")
#     if response.status_code != 200:
#         print("Error != 200")
#         print("Error != 200")
#         print("Error != 200")
#         print("Error != 200")
#     else:
#         return response.json()
#
#
# @api.multi
# def action_action(self):
#     zalo_info = ZaloOaInfo(oa_id=oa_id, secret_key=secret)
#     zalo_oa_client = ZaloOaClient(zalo_info)
#     profile = zalo_oa_client.get('getprofile', {'uid': 4812459256566519185})
#     self.get_social_acc()
#     data = {
#         'recipient': {'user_id': '2853770907771020226'},
#         'message': {'text': self.name}
#     }
#     params = {'data': data}
#     # send_text_message = zalo_oa_client.post('/sendmessage/text', params)
#     self.post('message', data, code)
#
#
# def get_social_acc(self):
#     zalo_info = ZaloAppInfo(app_id=app_id, secret_key=secret, callback_url=url)
#     zalo_3rd_app_client = Zalo3rdAppClient(zalo_info)
#     print(zalo_3rd_app_client)
#     login_url = zalo_3rd_app_client.get_login_url()
#     # print(login_url)
#     # access_token = zalo_3rd_app_client.get_access_token(access_token_social)
#     # access_token = access_token['access_token']
#     # print(access_token)
#     profile = zalo_3rd_app_client.get('/me', access_token_social, {'fields': 'id, name, birthday, gender, picture'})
#     friends = zalo_3rd_app_client.get('/me/friends', access_token_social, {'limit': 100})
#     invitable_friends = zalo_3rd_app_client.get('/me/invitable_friends', access_token_social, {
#         'offset': '0',
#         'limit': '1000',
#         'fields': 'id, name'
#     })
#     mr_hien = '2972427911927396120'
#     # mr.hien: 2972427911927396120
#     # mr.Manh: 2853770907771020226
#     print("Hello")