import logging

from education.common.logger import Logger
from education.constant.globalvar import BASE_URL
from education.interface.addwumodle import AddWuModel
from education.interface.basemethod import Base
from education.common.sendmethod import Method
from education.interface.publishmodle import Publish
from education.interface.addwginstance import AddWgInstance
import json

"""
注册物实例
"""


class AddModleInstance(Base):


    def __init__(self, method="post", url="/edu-portal-server/api/portal/thing/thing-instance/add"):
        super().__init__()
        self.logger = Logger(logging.INFO, logging.DEBUG)
        self.method = method
        self.url = BASE_URL + url
        self.modle = AddWuModel()
        self.publish = Publish()


    def data(self, thingModleId, gateWayThingId, type="DEVICE"):
        data = {
            "modelType": type,
            "name": "物模型实例" + self.rand(),
            "modelId": thingModleId,
            "assetId": self.rand(),
            "connectId": self.rand(),
            "connectType": "UNCONNECTED",
            "gatewayId": gateWayThingId
        }
        self.logger.info("新建物实例参数：{}".format(data))
        return data

    def post_add_mxInstance(self, thingModelId, gateWayThingId):
        self.publish.post_publish(thingModelId)
        response = Method.send_method(self.method, self.url, self.head, self.data(thingModelId, gateWayThingId))
        self.logger.info("注册物模型实例成功,物模型实例id为：{}".format(response.json()["data"]))
        return response.json()["data"]


if __name__ == '__main__':
    s = AddModleInstance()
