import asyncio
import logging

from education.common.logger import Logger
from education.constant.globalvar import BASE_URL
from education.interface.basemethod import Base
from education.common.sendmethod import Method
from education.tables.devices_models import BDeviceInfo
from education.update.connect_devices import Devices
import time


'''
读取数据库，启动设备
'''

class PublishDevices(Base):

    def __init__(self, method="get", url="/device-server/api/device/device/device-info/startDevice"):
        super().__init__()
        self.logger = Logger(logging.INFO, logging.DEBUG)
        self.method = method
        self.url = BASE_URL + url
        self.devicesObj = Devices()

    def param(self, devicesid):
        data = {"deviceId": devicesid}
        self.logger.info("虚拟设备启动参数:{}".format(data))
        return data
    '''
    启动设备
    '''
    def startDevices(self):
        devices = self.devicesObj.query(BDeviceInfo)
        lists = devices.filter_by(creator_true_name="定时发送", delete_flag=0, run_status=0).all()
        array = []
        for i in lists:
            array.append(i.id)
        for j in array:
            self.logger.info("获取虚拟设备id:{}".format(j))
            response = Method.send_method(self.method, self.url, self.head, self.param(j))
            time.sleep(1)
            self.logger.info("请求url：{}".format(response.url))
            self.logger.info("请求响应结果:{}".format(response.json()))
            if response.json()["code"] == 2000 and response.json()["success"] == True:
                self.logger.info("虚拟设备启动成功")
            else:
                continue

if __name__ == '__main__':
    async def running(i):
        print("-------------第{}个任务：任务开始启动---------------".format(i))
        startWork = PublishDevices()
        startWork.startDevices()

        await asyncio.sleep(i)
        print("------------第{}个设备启动完成-----------".format(i))


    async def report():
        print("------任务正在执行-------")


    loop = asyncio.get_event_loop()

    tasks = [
        asyncio.ensure_future(running(1)),
        asyncio.ensure_future(running(2)),
        asyncio.ensure_future(running(3)),
        asyncio.ensure_future(running(4)),
        asyncio.ensure_future(running(5)),
        asyncio.ensure_future(report())
    ]
    loop.run_until_complete(asyncio.wait(tasks))

