import logging

from education.common.logger import Logger
from education.constant.globalvar import getHeader, BASE_URL
from education.interface.login import Login
import random
from education.common.sendmethod import *
from education.interface.basemethod import Base

"""
添加网关模型
"""


class AddWgModel(Base):


    def __init__(self, method="post", url="/edu-portal-server/api/portal/thing/thing-model/add"):
        self.logger = Logger(logging.INFO, logging.DEBUG)
        super().__init__()
        self.method = method
        self.url = BASE_URL + url


    def add_model_param(self, type="GATEWAY"):
        random_str = str(random.randrange(1, 9999999999, 10))
        add_model_wg = {
            "isUseModel": False,
            "modelType": type,
            "name": "网关" + random_str
        }
        self.logger.info("新建网关参数：{}".format(add_model_wg))
        return add_model_wg

    def post_add_model(self):
        response = Method.send_method(self.method, self.url, self.head, self.add_model_param())
        self.logger.info("添加网关模型成功,网关模型id为：{}".format(response.json()["data"]))
        return response.json()["data"]

if __name__ == '__main__':
    a = AddWgModel()
