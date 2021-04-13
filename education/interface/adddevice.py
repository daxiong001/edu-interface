import logging

from education.common.wechat import *
from education.common.logger import Logger
from education.constant.globalvar import BASE_URL
from education.interface.basemethod import Base
from education.common.sendmethod import Method
from education.interface.devicetemplate import Template

"""
添加虚拟设备
"""


class AddDevices(Base):


    def __init__(self, method="post", url="/device-server/api/device/device/device-info/add"):
        super().__init__()
        self.logger = Logger(logging.INFO, logging.DEBUG)
        self.method = method
        self.url = BASE_URL + url
        self.template = Template()



    def add_devices_param(self):
        param = {
                "name": self.template.getdata()[0],
                "brand": "教学品牌",
                "modelNumber": "Rootcloud-Electric-meter01",
                "deviceSerialNum": self.template.getdata()[1],
                "power": "1.5W",
                "netModelNumber": "Rootcloud-gw01",
                "netBrand": "根云网关",
                "netSerialNum": self.template.getdata()[2],
                "protocolName": "ModbusTCP",
                "imageUrl": "dianbiao.png",
                "templateId": self.template.getdata()[3],
                "protocolId": 1
            }
        self.logger.info("新建虚拟设备参数：{}".format(param))
        return param

    def post_add_devices(self):
        response = Method.send_method(self.method, self.url, self.head, self.add_devices_param())
        self.logger.info("新建虚拟设备成功,设备id为：{}".format(response.json()["data"]))
        if response.status_code == 200:
            dict.append("> 新建虚拟设备接口：<font color=\"info\">通过</font> {}\n".format(response.json()))
        else:
            dict.append("> 新建虚拟设备接口：<font color=\"comment\">失败</font> \n")
        return response.json()["data"]

if __name__ == '__main__':
    a = AddDevices()
