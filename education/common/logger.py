import logging
import os
import time
import sys


class Logger(object):
    def __init__(self, clevel=logging.INFO, Flevel=logging.INFO):
        self.logger = logging.getLogger()
        self.logger.handlers.clear()
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_dir = os.path.join(os.path.dirname(os.getcwd()), '..\\log\\')
        fmt = logging.Formatter('%(asctime)s - %(name)s -%(funcName)s - %(levelname)s - %(message)s',
                                '%Y-%m-%d %H:%M:%S')
        log_name = log_dir + rq + ".log"
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
            # 设置文件日志
            fh = logging.FileHandler(log_name)
            fh.setFormatter(fmt)
            fh.setLevel(Flevel)
        else:
            # 设置文件日志
            fh = logging.FileHandler(log_name, encoding='utf-8')
            fh.setFormatter(fmt)
            fh.setLevel(Flevel)

        self.logger.setLevel(logging.INFO)

        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setLevel(clevel)
        sh.setFormatter(fmt)

        self.logger.addHandler(sh)
        # self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)
