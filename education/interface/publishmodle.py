import logging

from education.common.logger import Logger
from education.common.sendmethod import Method
from education.constant.globalvar import BASE_URL
from education.interface.basemethod import Base

"""
发布模型
"""


class Publish(Base):

    def __init__(self, method="post", url="/edu-portal-server/api/portal/thing/thing-model/publishById"):
        super().__init__()
        self.logger = Logger(logging.INFO, logging.DEBUG)
        self.method = method
        self.url = BASE_URL + url

    def data(self, id):
        data = {"id": id}
        self.logger.info("发布模型参数：{}".format(data))
        return data

    def post_publish(self, id):
        response = Method.send_method(self.method, self.url, self.head, self.data(id))
        self.logger.info("发布模型成功：{}".format(response.status_code))
        return response.status_code

