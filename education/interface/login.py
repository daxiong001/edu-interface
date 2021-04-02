import logging

from education.common.sendmethod import *
from education.constant.globalvar import getHeader, BASE_URL
import time
from education.common.logger import Logger

"""
登陆
"""


class Login(object):

    def __init__(self, method="post", url="/edu-portal-server/api/portal/base/user/login"):
        self.logger = Logger(logging.INFO, logging.DEBUG)
        self.url = BASE_URL + url
        self.head = getHeader(0, 2)
        self.method = method

    def login_data(self):
        data = {
            "mobile": "19999999999",
            "password": "IABSvX2Sc8aKVaDuK0CysPZCEDEjQpzbfWQvX9WmNw11GYp2/OkCgyv26IcjA8MEEB2lrM9amP+sB8uo471xTcE8GYar2jl71BGasgcQImQVnmagA/LRUjbvB00RhRRX3Gw22M8lnzlOl4j5andNikPyjroXhNzcU+BJYJHLcz0="
        }
        return data

    def login_response(self):
        # self.logger.info("登陆参数:{}".format(self.login_data()))
        response = Method.send_method(self.method, self.url, self.head, self.login_data())
        # self.logger.info("登陆响应结果:{}".format(response.json()))
        timestamp = lambda: int(time.time() * 1000)
        token = response.json()["data"]["token"] + str(timestamp())
        return token





if __name__ == '__main__':
    login = Login()
    token= login.login_response()
    print(token)
