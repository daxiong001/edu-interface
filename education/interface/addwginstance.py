import logging

from education.common.logger import Logger
from education.constant.globalvar import BASE_URL
from education.interface.addwgmodle import AddWgModel
from education.interface.basemethod import Base
from education.common.sendmethod import Method
from education.interface.publishmodle import Publish
from education.common.wechat import *

"""
注册网关实例
"""


class AddWgInstance(Base):

    def __init__(self, method="post", url="/edu-portal-server/api/portal/thing/thing-instance/add"):
        super().__init__()
        self.logger = Logger(logging.INFO, logging.DEBUG)
        self.method = method
        self.url = BASE_URL + url
        self.modle = AddWgModel()
        self.publish = Publish()

    def data(self, gateWayId, type="GATEWAY"):
        data = {
            "modelType": type,
            "name": "网关实例" + self.rand(),
            "modelId": gateWayId,
            "authId": self.rand(),
            "authToken": self.rand(),
            "simNumber": "",
            "assetId": self.rand()
        }
        self.logger.info("新建网关实例参数：{}".format(data))
        return data

    def post_add_wg(self, gateWayModleId):
        self.publish.post_publish(gateWayModleId)
        response = Method.send_method(self.method, self.url, self.head, self.data(gateWayModleId))
        self.logger.info("注册网关实例成功,网关实例id为：{}".format(response.json()["data"]))
        if response.status_code == 200:
            dict.append("> 新建网关实例接口：<font color=\"info\">通过</font>{} \n".format(response.json()))
        else:
            dict.append("> 新建网关实例接口：<font color=\"comment\">失败</font> \n")
        return response.json()["data"]


if __name__ == '__main__':
    s = AddWgInstance()
