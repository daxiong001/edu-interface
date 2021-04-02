import logging

from education.common.logger import Logger
from education.constant.globalvar import getHeader, BASE_URL
from education.interface.login import Login
import random
from education.common.sendmethod import *
from education.interface.basemethod import Base

"""
添加物模型
"""


class AddWuModel(Base):

    def __init__(self, method="post", url="/edu-portal-server/api/portal/thing/thing-model/add"):
        super().__init__()
        self.logger = Logger(logging.INFO, logging.DEBUG)
        self.method = method
        self.url = BASE_URL + url


    def add_modelwu_param(self, type="DEVICE"):
        random_str = str(random.randrange(1, 9999999999, 10))
        add_model_wg = {
            "isUseModel": True,
            "modelType": type,
            "name": "物模型" + random_str,
            "templateId": "4",
            "category": "机床,镗床",
            "connectType": "UNCONNECTED"
        }
        self.logger.info("新建物模型参数：{}".format(add_model_wg))
        return add_model_wg

    def post_add_modelwu(self):
        response = Method.send_method(self.method, self.url, self.head, self.add_modelwu_param())
        self.logger.info("新建物模型成功,物模型id为：{}".format(response.json()["data"]))
        return response.json()["data"]


if __name__ == '__main__':
    s = AddWuModel()
