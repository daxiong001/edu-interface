import logging

from education.common.logger import Logger
from education.constant.globalvar import BASE_URL
from education.interface.basemethod import Base
from education.common.sendmethod import Method

"""
选择虚拟设备模版
"""


class Template(Base):

    def __init__(self, method="get", url="/device-server/api/device/device/device-info/addPre"):
        super().__init__()
        self.logger = Logger(logging.INFO, logging.DEBUG)
        self.method = method
        self.url = BASE_URL + url

    def data(self, num="6"):
        param = {
            "templateId": num
        }
        # self.logger.info("获取虚拟设备模版：{}".format(param))
        return param

    def getdata(self):
        response = Method.send_method(self.method, self.url, self.head, self.data())
        # self.logger.info("获取虚拟设备模版成功：模版名称{0};设备号{1};网关编号{2};模版编号{3}".format(response.json()["data"]["name"], response.json()["data"]["deviceSerialNum"],
        #                                                                 response.json()["data"]["netSerialNum"], response.json()["data"]["templateId"]))
        return response.json()["data"]["name"], response.json()["data"]["deviceSerialNum"], \
               response.json()["data"]["netSerialNum"], response.json()["data"]["templateId"]




