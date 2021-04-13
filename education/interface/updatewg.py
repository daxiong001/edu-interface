import logging

from education.common.wechat import *
from education.common.logger import Logger
from education.common.sendmethod import Method
from education.interface.addwginstance import AddWgInstance
from education.interface.basemethod import Base
from education.update.connect_devices import Devices
from education.interface.adddevice import AddDevices
from education.tables.devices_models import BDeviceInfo
from education.update.connect_portal import Portal
from education.tables.portal_models import BThingInstance
from education.tables.devices_models import BDeviceNConfig
from education.constant.globalvar import BASE_URL
from education.interface.addwuinstance import AddModleInstance
from education.interface.addwgmodle import AddWgModel
from education.interface.addwumodle import AddWuModel


class UpdateWg(Base):



    def __init__(self, method="get", url="/device-server/api/device/device/device-info/startDevice"):
        super().__init__()
        self.logger = Logger(logging.INFO, logging.DEBUG)
        self.method = method
        self.url = BASE_URL + url
        self.devices = Devices()
        self.portal = Portal()
        self.gateWayId = AddWgModel().post_add_model()
        self.gateWayInstanceId = AddWgInstance().post_add_wg(self.gateWayId)
        self.modleId = AddWuModel().post_add_modelwu()
        self.modleInstanceId = AddModleInstance().post_add_mxInstance(self.modleId, self.gateWayInstanceId)
        self.devicesId = AddDevices().post_add_devices()



    '''
    查询虚拟设备网关与设备序列号
    '''
    def selectId(self):
        devicesInfo = self.devices.query(BDeviceInfo)
        use = devicesInfo.filter_by(id=self.devicesId).first()
        self.logger.info("查询虚拟设备参数，网关序列号：{};设备序列号：{}".format(str(use.net_serial_num), str(use.device_serial_num)))
        return use.net_serial_num, use.device_serial_num

    '''
    查询设备实例并更新字段值
    '''
    def selectInstance(self):
        #查询网关实例并更新物标识字段值
        instanceWgObj = self.portal.query(BThingInstance)
        wgObj = instanceWgObj.filter_by(id=self.gateWayInstanceId).first()
        self.logger.info("更新前网关序列号：{}".format(str(wgObj.asset_id)))
        wgObj.asset_id = self.selectId()[0]
        self.portal.commit()
        dict.append("> 更新网关实例序列号：<font color=\"info\">通过</font> 网关序列号：{}\n".format(str(wgObj.asset_id)))
        self.logger.info("更新后网关序列号：{}".format(str(wgObj.asset_id)))
        #查询物模型实例更新物标识字段值
        instanceMxObj = self.portal.query(BThingInstance)
        mxObj = instanceMxObj.filter_by(id=self.modleInstanceId).first()
        self.logger.info("更新前设备序列号：{}".format(str(mxObj.asset_id)))
        mxObj.asset_id = self.selectId()[1]
        self.portal.commit()
        dict.append("> 更新物实例设备序列号：<font color=\"info\">通过</font> 设备序列号：{}\n".format(str(mxObj.asset_id)))
        self.logger.info("更新后的设备序列号：{}".format(str(mxObj.asset_id)))



    '''查询实例的用户名和密码,更新到虚拟设备'''
    def updateDevices(self):
        '''
        查询到网关实例的用户名密码
        '''
        wggObjQuery = self.portal.query(BThingInstance)
        wgObj = wggObjQuery.filter_by(id=self.gateWayInstanceId).first()
        id = wgObj.auth_id
        pwd = wgObj.auth_token
        self.logger.info("查询网关实例的用户名：{}；密码；{}".format(id, pwd))
        '''
        查询到虚拟设备的信息
        '''
        sbObjQuery = self.devices.query(BDeviceNConfig)
        sbObj = sbObjQuery.filter_by(device_id=self.devicesId).first()
        sbObj.client_id = id
        sbObj.user_name = id
        sbObj.password = pwd
        self.devices.commit()
        dict.append("> 更新虚拟设备参数：<font color=\"info\">通过</font> client_id{};用户名{}；密码；{}\n".format(str(sbObj.client_id), str(sbObj.user_name), str(sbObj.password)))
        self.logger.info("虚拟设备对象赋值成功：client_id{};用户名{}；密码；{}".format(str(sbObj.client_id), str(sbObj.user_name), str(sbObj.password)))

    '''
    启动设备接口参数化
    '''
    def param(self, devicesid):
        data = {"deviceId": devicesid}
        self.logger.info("虚拟设备启动参数:{}".format(data))
        return data
    '''
    启动设备
    '''
    def startDevices(self):
        response = Method.send_method(self.method, self.url, self.head, self.param(self.devicesId))
        self.logger.info("虚拟设备启动成功:{}".format(response.status_code))
        if response.status_code == 200:
            dict.append("> 启动虚拟设备接口：<font color=\"info\">通过</font> {}\n".format(response.json()))
        else:
            dict.append("> 启动虚拟设备接口：<font color=\"comment\">失败</font> \n")
        return response.status_code


