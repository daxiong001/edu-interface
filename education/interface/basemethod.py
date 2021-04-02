from education.constant.globalvar import getHeader, BASE_URL
from education.interface.login import Login
import random

"""
基础类
"""

class Base(object):

    def __init__(self):
        self.login = Login()
        self.head = getHeader(2, 2, self.login.login_response())

    def rand(self):
        random_str = str(random.randrange(1, 9999999999, 10))
        return random_str

