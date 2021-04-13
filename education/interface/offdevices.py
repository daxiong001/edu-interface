import logging

from education.common.logger import Logger
from education.constant.globalvar import BASE_URL
from education.interface.basemethod import Base
from education.common.sendmethod import Method
from education.tables.devices_models import BDeviceInfo
from education.update.connect_devices import Devices
from sqlalchemy import text

'''
读取数据库，关闭设备
'''


class OffDevices(Base):

    def __init__(self, method="get", url="/device-server/api/device/device/device-info/stopDevice"):
        super().__init__()
        self.logger = Logger(logging.INFO, logging.DEBUG)
        self.method = method
        self.url = BASE_URL + url
        self.devicesObj = Devices()

    def param(self, devicesid):
        data = {"deviceId": devicesid}
        self.logger.info("虚拟设备关闭参数:{}".format(data))
        return data

    '''
    启动设备
    '''

    def offDevices(self):
        devices = self.devicesObj.query(BDeviceInfo)
        lists = devices.filter_by(creator_true_name="定时发送", delete_flag=0, run_status=1).all()
        array = []
        for i in lists:
            array.append(i.id)
        for j in array:
            self.logger.info("获取虚拟设备id:{}".format(j))
            response = Method.send_method(self.method, self.url, self.head, self.param(j))
            self.logger.info("请求url：{}".format(response.url))
            self.logger.info("请求响应结果:{}".format(response.json()))
            if response.json()["code"] == 2000 and response.json()["success"] == True:
                self.logger.info("虚拟设备关闭成功")


if __name__ == '__main__':
    a = OffDevices()
    a.offDevices()
