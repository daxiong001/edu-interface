# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, DateTime, ForeignKeyConstraint, Index, LargeBinary, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, SMALLINT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class QRTZCALENDAR(Base):
    __tablename__ = 'QRTZ_CALENDARS'

    SCHED_NAME = Column(String(120), primary_key=True, nullable=False)
    CALENDAR_NAME = Column(String(190), primary_key=True, nullable=False)
    CALENDAR = Column(LargeBinary, nullable=False)


class QRTZFIREDTRIGGER(Base):
    __tablename__ = 'QRTZ_FIRED_TRIGGERS'
    __table_args__ = (
        Index('IDX_QRTZ_FT_JG', 'SCHED_NAME', 'JOB_GROUP'),
        Index('IDX_QRTZ_FT_T_G', 'SCHED_NAME', 'TRIGGER_NAME', 'TRIGGER_GROUP'),
        Index('IDX_QRTZ_FT_INST_JOB_REQ_RCVRY', 'SCHED_NAME', 'INSTANCE_NAME', 'REQUESTS_RECOVERY'),
        Index('IDX_QRTZ_FT_TRIG_INST_NAME', 'SCHED_NAME', 'INSTANCE_NAME'),
        Index('IDX_QRTZ_FT_TG', 'SCHED_NAME', 'TRIGGER_GROUP'),
        Index('IDX_QRTZ_FT_J_G', 'SCHED_NAME', 'JOB_NAME', 'JOB_GROUP')
    )

    SCHED_NAME = Column(String(120), primary_key=True, nullable=False)
    ENTRY_ID = Column(String(95), primary_key=True, nullable=False)
    TRIGGER_NAME = Column(String(190), nullable=False)
    TRIGGER_GROUP = Column(String(190), nullable=False)
    INSTANCE_NAME = Column(String(190), nullable=False)
    FIRED_TIME = Column(BIGINT(13), nullable=False)
    SCHED_TIME = Column(BIGINT(13), nullable=False)
    PRIORITY = Column(INTEGER(11), nullable=False)
    STATE = Column(String(16), nullable=False)
    JOB_NAME = Column(String(190))
    JOB_GROUP = Column(String(190))
    IS_NONCONCURRENT = Column(String(1))
    REQUESTS_RECOVERY = Column(String(1))


class QRTZJOBDETAIL(Base):
    __tablename__ = 'QRTZ_JOB_DETAILS'
    __table_args__ = (
        Index('IDX_QRTZ_J_GRP', 'SCHED_NAME', 'JOB_GROUP'),
        Index('IDX_QRTZ_J_REQ_RECOVERY', 'SCHED_NAME', 'REQUESTS_RECOVERY')
    )

    SCHED_NAME = Column(String(120), primary_key=True, nullable=False)
    JOB_NAME = Column(String(190), primary_key=True, nullable=False)
    JOB_GROUP = Column(String(190), primary_key=True, nullable=False)
    DESCRIPTION = Column(String(250))
    JOB_CLASS_NAME = Column(String(250), nullable=False)
    IS_DURABLE = Column(String(1), nullable=False)
    IS_NONCONCURRENT = Column(String(1), nullable=False)
    IS_UPDATE_DATA = Column(String(1), nullable=False)
    REQUESTS_RECOVERY = Column(String(1), nullable=False)
    JOB_DATA = Column(LargeBinary)


class QRTZLOCK(Base):
    __tablename__ = 'QRTZ_LOCKS'

    SCHED_NAME = Column(String(120), primary_key=True, nullable=False)
    LOCK_NAME = Column(String(40), primary_key=True, nullable=False)


class QRTZPAUSEDTRIGGERGRP(Base):
    __tablename__ = 'QRTZ_PAUSED_TRIGGER_GRPS'

    SCHED_NAME = Column(String(120), primary_key=True, nullable=False)
    TRIGGER_GROUP = Column(String(190), primary_key=True, nullable=False)


class QRTZSCHEDULERSTATE(Base):
    __tablename__ = 'QRTZ_SCHEDULER_STATE'

    SCHED_NAME = Column(String(120), primary_key=True, nullable=False)
    INSTANCE_NAME = Column(String(190), primary_key=True, nullable=False)
    LAST_CHECKIN_TIME = Column(BIGINT(13), nullable=False)
    CHECKIN_INTERVAL = Column(BIGINT(13), nullable=False)


class BBaseDept(Base):
    __tablename__ = 'b_base_dept'
    __table_args__ = {'comment': '组织表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    parent_id = Column(BIGINT(20), nullable=False, comment='#父级组织id#')
    school_id = Column(BIGINT(20), nullable=False, comment='#学校id#')
    status = Column(TINYINT(4), nullable=False, comment='#状态#ENUM#1:有效:ENABLE,2:失效:DISABLE#')
    ancestors = Column(String(1000), nullable=False, comment='#祖级列表#')
    name = Column(String(50), nullable=False, comment='#组织名称#')
    order_num = Column(INTEGER(11), comment='#排序#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BBaseDeptUser(Base):
    __tablename__ = 'b_base_dept_user'
    __table_args__ = {'comment': '组织用户关联表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    school_id = Column(BIGINT(20), nullable=False, comment='#学校id#REF#b_base_school.id#')
    dept_id = Column(BIGINT(20), nullable=False, comment='#组织id#REF#b_base_dept.id#')
    user_id = Column(BIGINT(20), nullable=False, comment='#用户id#REF#b_base_user.id#')
    role = Column(TINYINT(4), nullable=False, comment='#角色#ENUM#1:平台管理员:PLATFORM_ADMIN,2:学校管理员:COLLEGE_ADMIN,3:老师:TEACHER,4:学生:STUDENT,5:游客:TOURIST#')
    admin = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='#是否为组织管理员#')
    last_login = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='#是否为上次登录#')
    display = Column(TINYINT(1), nullable=False, server_default=text("'1'"), comment='#是否显示#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BBaseMenu(Base):
    __tablename__ = 'b_base_menu'
    __table_args__ = {'comment': '菜单表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    parent_id = Column(BIGINT(20), nullable=False, comment='#上级id#')
    menu_code = Column(String(100), comment='#编号#')
    menu_name = Column(String(100), nullable=False, comment='#菜单名称#')
    order_num = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='#排序#')
    menu_path = Column(String(200), comment='#菜单地址#')
    auth_path = Column(String(255), comment='#权限地址#')
    type = Column(TINYINT(4), nullable=False, comment='#菜单类型#ENUM#1:菜单:MENU,2:按钮:BUTTON#')
    icon = Column(String(200), comment='#菜单图标#')
    remark = Column(String(255), comment='#备注#')
    display = Column(TINYINT(1), server_default=text("'1'"), comment='#是否展示#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BBaseRole(Base):
    __tablename__ = 'b_base_role'
    __table_args__ = {'comment': '角色表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    version_id = Column(BIGINT(20), comment='#版本id#REF#b_base_version.id#')
    name = Column(String(100), nullable=False, comment='#角色名称#')
    code = Column(String(100), nullable=False, server_default=text("'0'"), comment='#角色编码#')
    remark = Column(String(200), comment='#备注#')
    status = Column(TINYINT(4), nullable=False, server_default=text("'0'"), comment='#状态#ENUM#1:启用:ENABLE,2:停用:DISABLE#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BBaseRoleMenu(Base):
    __tablename__ = 'b_base_role_menu'
    __table_args__ = {'comment': '角色菜单关联表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    role_id = Column(BIGINT(20), nullable=False, comment='#角色id#RFE#b_base_role.id#')
    menu_id = Column(BIGINT(20), nullable=False, comment='#菜单id#REF#b_base_menu.id#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BBaseSchool(Base):
    __tablename__ = 'b_base_school'
    __table_args__ = {'comment': '学校表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    no = Column(String(50), nullable=False, unique=True, comment='#编号#')
    name = Column(String(50), nullable=False, comment='#学校名称#')
    tid = Column(String(50), comment='#纳税人识别码#')
    industry = Column(String(100), comment='#所属行业#')
    email = Column(String(100), nullable=False, comment='#邮箱#')
    wechat = Column(String(100), comment='#微信#')
    tel = Column(String(100), comment='#电话#')
    fax = Column(String(100), comment='#传真#')
    address = Column(String(100), comment='#详细地址#')
    detail_desc = Column(String(1024), comment='#详细描述#')
    effective_deadline = Column(Date, comment='#有效截止日#')
    member_number = Column(INTEGER(11), comment='#成员个数#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BBaseSchoolUser(Base):
    __tablename__ = 'b_base_school_user'
    __table_args__ = {'comment': '学校用户关联表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    school_id = Column(BIGINT(20), nullable=False, comment='#学校id#REF#b_base_school.id#')
    user_id = Column(BIGINT(20), nullable=False, comment='#用户id#REF#b_base_user.id#')
    admin = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='#是否为组织管理员#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BBaseSmsRecord(Base):
    __tablename__ = 'b_base_sms_record'
    __table_args__ = {'comment': '短信记录表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键#')
    code = Column(String(20), comment='#验证码#')
    mobile = Column(String(20), comment='#手机号#')
    minute = Column(String(10), comment='#有效时间#')
    response = Column(Text, comment='#短信发送结果#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseUser(Base):
    __tablename__ = 'b_base_user'
    __table_args__ = {'comment': '用户表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    type = Column(TINYINT(4), nullable=False, server_default=text("'0'"), comment='#用户类型#ENUM#1:平台管理员:PLATFORM_ADMIN,2:学校用户:COLLEGE_USER,3:游客:TOURIST#')
    status = Column(TINYINT(4), nullable=False, comment='#用户状态#ENUM#1:未激活:UN_ACTIVE,2:已激活:ACTIVE#')
    username = Column(String(50), nullable=False, comment='#用户名#')
    password = Column(String(100), nullable=False, comment='#密码#')
    real_name = Column(String(50), comment='#真实姓名#')
    nickname = Column(String(50), comment='#昵称#')
    mobile = Column(String(11), comment='#手机#')
    email = Column(String(100), comment='#邮箱#')
    position = Column(String(50), comment='#岗位#')
    sex = Column(TINYINT(4), comment='#性别#ENUM#1:男:MALE,2:女:FEMALE,3:未知:UNKNOWN#')
    birthday = Column(DateTime, comment='#生日#')
    avatar_url = Column(String(1000), comment='#头像url#')
    address = Column(String(200), comment='#地址#')
    contact_number = Column(String(50), comment='#联系电话#')
    first_login_time = Column(DateTime, comment='#第一次登录时间#')
    last_login_time = Column(DateTime, comment='#最后登录时间#')
    update_pwd = Column(TINYINT(1), comment='#是否修改过密码#')
    remark = Column(String(255), comment='#备注#')
    device_guide = Column(TINYINT(1), comment='#设备指引#')
    portal_guide = Column(TINYINT(1), comment='#门户指引#')
    visual_guide = Column(TINYINT(1), comment='#可视化指引#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BBaseUserRole(Base):
    __tablename__ = 'b_base_user_role'
    __table_args__ = {'comment': '用户角色表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    user_id = Column(BIGINT(20), nullable=False, comment='#用户id#REF#b_base_user.id#')
    role_id = Column(BIGINT(20), nullable=False, comment='#角色id#REF#b_base_role.id#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BBaseVersion(Base):
    __tablename__ = 'b_base_version'
    __table_args__ = {'comment': '版本表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键#')
    name = Column(String(128), nullable=False, unique=True, server_default=text("''"), comment='#版本名称#')
    remark = Column(String(512), server_default=text("''"), comment='#版本说明#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseVersionMenu(Base):
    __tablename__ = 'b_base_version_menu'
    __table_args__ = {'comment': '版本菜单表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键#')
    version_id = Column(BIGINT(20), nullable=False, index=True, comment='#版本id#REF#b_base_version_menu.id#')
    menu_id = Column(BIGINT(20), nullable=False, comment='#菜单id#REF#b_base_menu.id#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseVersionSchool(Base):
    __tablename__ = 'b_base_version_school'
    __table_args__ = {'comment': '版本学校表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键#')
    version_id = Column(BIGINT(20), nullable=False, index=True, comment='#版本id#REF#b_base_version.id#')
    school_id = Column(BIGINT(20), nullable=False, comment='#学校id#REF#b_base_school.id#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BResourceFile(Base):
    __tablename__ = 'b_resource_file'
    __table_args__ = {'comment': '文件表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    file_storage_id = Column(String(25), comment='#文件服务器存储的id#')
    type = Column(TINYINT(4), comment='#文件类型#ENUM#1:图片:PICTURE,2:文件:FILE#')
    name = Column(String(500), nullable=False, comment='#图片名#')
    extension = Column(String(10), nullable=False, comment='#拓展名#')
    url = Column(String(200), nullable=False, comment='#文件服务器url#')
    path = Column(String(200), comment='#服务器绝对路径#')
    byte_size = Column(BIGINT(20), comment='#字节大小#')
    version = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='#版本号#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BThingDraftModel(Base):
    __tablename__ = 'b_thing_draft_model'
    __table_args__ = {'comment': '物模型主(草稿)表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_model.id#')
    code_id = Column(String(50), nullable=False, comment='#编号#模型ID#')
    name = Column(String(100), nullable=False, comment='#模型名称#')
    model_type = Column(TINYINT(4), server_default=text("'1'"), comment='#模型类型#ENUM#1:设备:DEVICE,2:网关:GATEWAY,3:复合物:COMPOUND#')
    connect_type = Column(TINYINT(4), server_default=text("'1'"), comment='#连接类型#ENUM#1:非直连:UNCONNECTED,2:直连:CONNECTED#')
    publish_status = Column(TINYINT(4), server_default=text("'1'"), comment='#发布状态#ENUM#1:未发布:UNPUBLISHED,2:已发布:PUBLISHED#')
    detection_period = Column(INTEGER(11), comment='#接入信息#离线检测周期(秒)#')
    unit_type = Column(TINYINT(4), comment='#接入信息#工况生成时间最小单位#ENUM#1:毫秒:MILLISECOND,2:秒:SECOND#')
    sample_period = Column(INTEGER(11), comment='#接入信息#下采样周期(秒)#')
    description = Column(String(500), comment='#描述说明#')
    visual_url = Column(String(500), comment='#可视化URL#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingDraftModelAlarm(Base):
    __tablename__ = 'b_thing_draft_model_alarm'
    __table_args__ = {'comment': '物模型报警(草稿)表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_model.id#')
    model_alarm_id = Column(BIGINT(20), comment='#物模型报警id#REF#b_thing_model_alarm.id#')
    name = Column(String(100), nullable=False, comment='#报警名称#')
    alarm_id = Column(String(100), nullable=False, comment='#报警ID#')
    description = Column(String(500), comment='#描述#')
    alarm_level_type = Column(TINYINT(4), server_default=text("'4'"), comment='#报警级别类型#ENUM#1:紧急:URGENCY,2:重要:IMPORTANT,3:警告:WARNING,4:一般:GENERAL,5:不确定:UNSURE#')
    label = Column(String(255), comment='#报警标签#数组字符串#')
    trigger_rule_json = Column(Text, comment='#设置报警触发规则json字符串#')
    property_id = Column(String(255), comment='#与报警同时上报的属性id数组#')
    reason = Column(Text, comment='#原因/解决方案#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingDraftModelInfo(Base):
    __tablename__ = 'b_thing_draft_model_info'
    __table_args__ = {'comment': '物模型基本信息(草稿)表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_model.id#')
    model_info_id = Column(BIGINT(20), nullable=False, comment='#物模型基本信息id#REF#b_thing_model_info.id#')
    title = Column(String(100), nullable=False, comment='#信息标题#')
    data_type = Column(String(20), server_default=text("'String'"), comment='#数据类型#')
    info_id = Column(String(100), nullable=False, comment='#信息ID#')
    info_value = Column(String(100), comment='#信息值#')
    status = Column(TINYINT(4), server_default=text("'1'"), comment='#允许实例处修改#ENUM#0:不允许,1:允许#')
    info_type = Column(TINYINT(4), server_default=text("'1'"), comment='#信息创建标识#ENUM#1:系统,2:手动#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingDraftModelInstruction(Base):
    __tablename__ = 'b_thing_draft_model_instruction'
    __table_args__ = {'comment': '物模型指令(草稿)表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_model.id#')
    model_instruction_id = Column(BIGINT(20), comment='#物模型指令id#REF#b_thing_model_instruction.id#')
    name = Column(String(100), nullable=False, comment='#指令名称#')
    instruction_id = Column(String(100), nullable=False, comment='#指令ID#')
    time_out = Column(INTEGER(11), server_default=text("'0'"), comment='#命令超时时间(秒)#')
    controlled_property = Column(Text, comment='#受控属性#数组字符串#')
    description = Column(String(500), comment='#描述#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingDraftModelNode(Base):
    __tablename__ = 'b_thing_draft_model_node'
    __table_args__ = {'comment': '复合物节点表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键#')
    model_id = Column(BIGINT(20), nullable=False, comment='#复合物的模型id#REF#b_thing_model.id#')
    model_node_id = Column(BIGINT(20), comment='#复合物的模型节点id#REF#b_thing_model_node.id#')
    name = Column(String(64), nullable=False, comment='#节点名称#')
    code_id = Column(String(64), nullable=False, comment='#设备节点code id#')
    node_model_id = Column(BIGINT(20), nullable=False, comment='#节点的设备模型id#REF#b_thing_model.id#')
    multiple_instance_flag = Column(TINYINT(1), nullable=False, comment='#是否可以部署多个实例#ENUM#0:否,1:是#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingDraftModelProperty(Base):
    __tablename__ = 'b_thing_draft_model_property'
    __table_args__ = {'comment': '物模型属性(草稿)表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_model.id#')
    model_property_id = Column(BIGINT(20), comment='#物模型属性id#REF#b_thing_model_property.id#')
    name = Column(String(100), nullable=False, comment='#属性名称#')
    property_id = Column(String(100), nullable=False, comment='#属性ID#')
    data_type = Column(TINYINT(4), server_default=text("'1'"), comment='#数据类型#ENUM#1:String,2:Number,3:Boolean,4:Integer,5:Binary,6:Json#')
    read_write_type = Column(TINYINT(4), server_default=text("'1'"), comment='#读写类型#ENUM#1:读写:READ_WRITE,2:只读:ONLY_READ,3:只写:ONLY_READ#')
    minimum = Column(String(100), comment='#取值范围#最小值#')
    maximum = Column(String(100), comment='#取值范围#最大值#')
    source_type = Column(TINYINT(4), server_default=text("'1'"), comment='#属性值来源类型#ENUM#1:连接变量:LINK_VARIABLE,2:规则指定:RULES_SPECIFY,3:手动写值:WRITE_VALUE#')
    source_json = Column(Text, comment='#属性值来源json字符串#')
    digits_type = Column(TINYINT(4), server_default=text("'1'"), comment='#小数点保留位数类型#ENUM#1:0位:ZERO,2:1位:ONE,3:2位:TWO,4:3位:THREE,5:4位:FOUR,6:5位:FIVE#')
    save_type = Column(TINYINT(4), server_default=text("'1'"), comment='#历史数据保存方式类型#ENUM#1:上报保存:REPORT,2:周期保存:PERIOD,3:变化保存:CHANGE,4:全部保存:ALL,5:不保存:NO#')
    unit = Column(String(100), comment='#工程单位#')
    label = Column(String(255), comment='#属性标签#数组字符串#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingInstance(Base):
    __tablename__ = 'b_thing_instance'
    __table_args__ = {'comment': '物实例主表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    school_id = Column(BIGINT(20), nullable=False, comment='#所属学校id#REF#b_base_school.id#')
    dept_id = Column(BIGINT(20), nullable=False, comment='#所属班级id#REF#b_base_dept.id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_model.id#')
    gateway_id = Column(BIGINT(20), comment='#物实例网关id#REF#b_thing_instance.id#')
    code_id = Column(String(50), nullable=False, comment='#编号#')
    name = Column(String(100), nullable=False, comment='#实例名称#')
    asset_id = Column(String(100), nullable=False, comment='#物标识#')
    connect_id = Column(String(100), comment='#通讯标识#')
    model_type = Column(TINYINT(4), server_default=text("'1'"), comment='#实例类型#ENUM#1:设备:DEVICE,2:网关:GATEWAY,3:复合物:COMPOUND#')
    connect_type = Column(TINYINT(4), server_default=text("'1'"), comment='#连接类型#ENUM#1:非直连:UNCONNECTED,2:直连:CONNECTED#')
    category = Column(String(100), comment='#基本信息#分类#')
    manufacturer = Column(String(100), comment='#基本信息#厂商#')
    model = Column(String(100), comment='#基本信息#型号#')
    fw_version = Column(String(100), comment='#基本信息#固件版本#')
    hw_version = Column(String(100), comment='#基本信息#硬件版本#')
    protocol = Column(String(100), server_default=text("'ROOTCLOUD_V4'"), comment='#支持协议#')
    auth_id = Column(String(100), comment='#认证标识#')
    auth_token = Column(String(100), comment='#认证密钥#')
    sim_number = Column(String(100), comment='#SIM卡IMSI号#')
    label = Column(String(500), comment='#标签#数组字符串#')
    description = Column(String(500), comment='#描述说明#')
    online_status = Column(TINYINT(4), server_default=text("'3'"), comment='#在线状态#ENUM#1:在线:ON_LINE,2:离线:OFF_LINE,3:未激活:INACTIVE#')
    online_time = Column(DateTime, comment='#在线时间#')
    first_up_time = Column(DateTime, comment='#首次上数时间#')
    write_value_json = Column(Text, comment='#属性#手动写值json字符串#{["property_id":"1","value":"1"]}#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DATETIME(fsp=3), comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DATETIME(fsp=3), comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingInstanceHistoryAlarm(Base):
    __tablename__ = 'b_thing_instance_history_alarm'
    __table_args__ = {'comment': '物实例历史报警表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    instance_id = Column(BIGINT(20), nullable=False, comment='#物实例id#REF#b_thing_instance.id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_model.id#')
    model_alarm_id = Column(BIGINT(20), nullable=False, comment='#物模型报警id#REF#b_thing_model_alarm.id#')
    property_report_json = Column(Text, comment='#上报的属性json#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DATETIME(fsp=3), comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DATETIME(fsp=3), comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingInstanceHistoryInstruction(Base):
    __tablename__ = 'b_thing_instance_history_instruction'
    __table_args__ = {'comment': '物实例历史指令表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    instance_id = Column(BIGINT(20), nullable=False, comment='#物实例id#REF#b_thing_instance.id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_model.id#')
    instruction_id = Column(BIGINT(20), nullable=False, comment='#物模型指令id#REF#b_thing_model_instruction.id#')
    property_report_json = Column(Text, comment='#执行的属性json#')
    trigger_type = Column(TINYINT(4), server_default=text("'1'"), comment='#触发方式类型#ENUM#1:手动触发:MANUAL,2:自动触发:AUTO#')
    result_type = Column(TINYINT(4), server_default=text("'4'"), comment='#执行结果类型#ENUM#1:执行超时:TIMEOUT,2:执行失败:FAIL,3:执行成功:NORMAL,4:执行中:RUNNING#')
    result = Column(String(255), comment='#执行结果JSON#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DATETIME(fsp=3), comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DATETIME(fsp=3), comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingInstanceNode(Base):
    __tablename__ = 'b_thing_instance_node'
    __table_args__ = {'comment': '复合物实例节点表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键#')
    instance_id = Column(BIGINT(20), nullable=False, index=True, comment='#复合物实例id#REF#b_thing_instance.id#')
    model_id = Column(BIGINT(20), nullable=False, index=True, comment='#复合物模型id#REF#b_thing_model.id#')
    model_node_id = Column(BIGINT(20), nullable=False, index=True, comment='#复合物模型节点id#REF#b_thing_model_node.id#')
    node_instance_id = Column(BIGINT(20), nullable=False, index=True, comment='#节点实例id#REF#b_thing_instance.id#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingLabel(Base):
    __tablename__ = 'b_thing_label'
    __table_args__ = {'comment': '标签表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    label_name = Column(String(100), nullable=False, comment='#标签名#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingLabelRelevance(Base):
    __tablename__ = 'b_thing_label_relevance'
    __table_args__ = {'comment': '标签关联表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    relevance_id = Column(BIGINT(20), nullable=False, comment='#关联标签的主键ID#')
    label_id = Column(BIGINT(20), comment='#标签ID#REF#b_thing_label_relevance.id#')
    label_name = Column(String(100), nullable=False, comment='#标签名(冗余)#')
    relevance_type = Column(TINYINT(4), nullable=False, comment='#关联类型#ENUM#1:属性:PROPERTY,2:报警:ALARM,3:实例:INSTANCE#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingModel(Base):
    __tablename__ = 'b_thing_model'
    __table_args__ = {'comment': '物模型主表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    school_id = Column(BIGINT(20), nullable=False, comment='#所属学校id#REF#b_base_school.id#')
    dept_id = Column(BIGINT(20), nullable=False, comment='#所属班级id#REF#b_base_dept.id#')
    code_id = Column(String(50), nullable=False, comment='#编号#模型ID#')
    name = Column(String(100), nullable=False, comment='#模型名称#')
    model_type = Column(TINYINT(4), server_default=text("'1'"), comment='#模型类型#ENUM#1:设备:DEVICE,2:网关:GATEWAY,3:复合物:COMPOUND#')
    connect_type = Column(TINYINT(4), server_default=text("'1'"), comment='#连接类型#ENUM#1:非直连:UNCONNECTED,2:直连:CONNECTED#')
    publish_status = Column(TINYINT(4), server_default=text("'1'"), comment='#发布状态#ENUM#1:未发布:UNPUBLISHED,2:已发布:PUBLISHED#')
    detection_period = Column(INTEGER(11), comment='#接入信息#离线检测周期(秒)#')
    unit_type = Column(TINYINT(4), comment='#接入信息#工况生成时间最小单位#ENUM#1:毫秒:MILLISECOND,2:秒:SECOND#')
    sample_period = Column(INTEGER(11), comment='#接入信息#下采样周期(秒)#')
    description = Column(String(500), comment='#描述说明#')
    visual_url = Column(String(500), comment='#可视化URL#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DATETIME(fsp=3), comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DATETIME(fsp=3), comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingModelAlarm(Base):
    __tablename__ = 'b_thing_model_alarm'
    __table_args__ = {'comment': '物模型报警表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_model.id#')
    name = Column(String(100), nullable=False, comment='#报警名称#')
    alarm_id = Column(String(100), nullable=False, comment='#报警ID#')
    description = Column(String(500), comment='#描述#')
    alarm_level_type = Column(TINYINT(4), server_default=text("'4'"), comment='#报警级别类型#ENUM#1:紧急:URGENCY,2:重要:IMPORTANT,3:警告:WARNING,4:一般:GENERAL,5:不确定:UNSURE#')
    label = Column(String(255), comment='#报警标签#数组字符串#')
    trigger_rule_json = Column(Text, comment='#设置报警触发规则json字符串#')
    property_id = Column(String(255), comment='#与报警同时上报的属性id数组#')
    reason = Column(Text, comment='#原因/解决方案#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingModelCategory(Base):
    __tablename__ = 'b_thing_model_category'
    __table_args__ = {'comment': '物模型分类表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    parent_id = Column(BIGINT(20), server_default=text("'0'"), comment='#一级分类的主键id#')
    name = Column(String(100), nullable=False, comment='#分类名称#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingModelInfo(Base):
    __tablename__ = 'b_thing_model_info'
    __table_args__ = {'comment': '物模型基本信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_model.id#')
    title = Column(String(100), nullable=False, comment='#信息标题#')
    data_type = Column(String(20), server_default=text("'String'"), comment='#数据类型#')
    info_id = Column(String(100), nullable=False, comment='#信息ID#')
    info_value = Column(String(100), comment='#信息值#')
    status = Column(TINYINT(4), server_default=text("'1'"), comment='#允许实例处修改#ENUM#0:不允许,1:允许#')
    info_type = Column(TINYINT(4), server_default=text("'1'"), comment='#信息创建标识#ENUM#1:系统,2:手动#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingModelInstruction(Base):
    __tablename__ = 'b_thing_model_instruction'
    __table_args__ = {'comment': '物模型指令表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_model.id#')
    name = Column(String(100), nullable=False, comment='#指令名称#')
    instruction_id = Column(String(100), nullable=False, comment='#指令ID#')
    time_out = Column(INTEGER(11), server_default=text("'0'"), comment='#命令超时时间(秒)#')
    controlled_property = Column(Text, comment='#受控属性#数组字符串#')
    description = Column(String(500), comment='#描述#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingModelNode(Base):
    __tablename__ = 'b_thing_model_node'
    __table_args__ = {'comment': '复合物节点表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键#')
    model_id = Column(BIGINT(20), nullable=False, comment='#复合物的模型id#REF#b_thing_model.id#')
    name = Column(String(64), nullable=False, comment='#节点名称#')
    code_id = Column(String(64), nullable=False, comment='#设备节点code id#')
    node_model_id = Column(BIGINT(20), nullable=False, comment='#节点的设备模型id#REF#b_thing_model.id#')
    multiple_instance_flag = Column(TINYINT(1), nullable=False, comment='#是否可以部署多个实例#ENUM#0:否,1:是#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingModelProperty(Base):
    __tablename__ = 'b_thing_model_property'
    __table_args__ = {'comment': '物模型属性表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_model.id#')
    name = Column(String(100), nullable=False, comment='#属性名称#')
    property_id = Column(String(100), nullable=False, comment='#属性ID#')
    data_type = Column(TINYINT(4), server_default=text("'1'"), comment='#数据类型#ENUM#1:String,2:Number,3:Boolean,4:Integer,5:Binary,6:Json#')
    read_write_type = Column(TINYINT(4), server_default=text("'1'"), comment='#读写类型#ENUM#1:读写:READ_WRITE,2:只读:ONLY_READ,3:只写:ONLY_READ#')
    minimum = Column(String(100), comment='#取值范围#最小值#')
    maximum = Column(String(100), comment='#取值范围#最大值#')
    source_type = Column(TINYINT(4), server_default=text("'1'"), comment='#属性值来源类型#ENUM#1:连接变量:LINK_VARIABLE,2:规则指定:RULES_SPECIFY,3:手动写值:WRITE_VALUE#')
    source_json = Column(Text, comment='#属性值来源json字符串#')
    digits_type = Column(TINYINT(4), server_default=text("'1'"), comment='#小数点保留位数类型#ENUM#1:0位:ZERO,2:1位:ONE,3:2位:TWO,4:3位:THREE,5:4位:FOUR,6:5位:FIVE#')
    save_type = Column(TINYINT(4), server_default=text("'1'"), comment='#历史数据保存方式类型#ENUM#1:上报保存:REPORT,2:周期保存:PERIOD,3:变化保存:CHANGE,4:全部保存:ALL,5:不保存:NO#')
    unit = Column(String(100), comment='#工程单位#')
    label = Column(String(255), comment='#属性标签#数组字符串#')
    io_code = Column(String(10), comment='#采集点编号#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingModelPropertyMethod(Base):
    __tablename__ = 'b_thing_model_property_method'

    id = Column(BIGINT(20), primary_key=True, comment='#主键#')
    property_name = Column(String(32), nullable=False, comment='#属性名称#')
    property_id = Column(String(20), nullable=False, comment='#属性id,注意：和其他表字段没有外键关系#')
    property_type = Column(TINYINT(4), nullable=False, comment='#属性数据类型#ENUM#1:整型:integer,2:数值:number,3:整型或数值:integer_number#')
    property_read_write = Column(TINYINT(4), nullable=False, comment='#读写操作#ENUM#1:只读:read_only,2:读写:read_write#')
    method_type = Column(TINYINT(4), nullable=False, comment='#方法类型#ENUM#1:calDeviceStatus:CAL_DEVICE_STATUS,2:calElapsedTime:CAL_ELAPSED_TIME,3:calRunningRatio:CAL_RUNNING_RATIO,4:calWorkingRatio:CAL_WORKING_RATIO,5:countshift:COUNT_SHIFT,6:calProductionCycle:CAL_PRODUCTION_CYCLE,7:totalEqpNum:TOTAL_EQP_NUM,8:calEqpNum:CAL_EQP_NUM,9:+:PLUS,10:-:SUBSTRACT,11:*:MULTIPLY,12:/:DIVIDE #')
    method_param_type = Column(String(32), nullable=False, comment='#方法参数类型列表json#ENUM#1:属性id:PROPERTY_ID,2:整型:INTEGER,3:布尔类型，0或1:BOOLEAN_INTEGER#')
    method_example = Column(String(128), nullable=False, comment='#方法示例#')
    use_scope = Column(TINYINT(4), nullable=False, comment='#使用范围#ENUM#1:设备:DEVICE,2:网关:GATEWAY,3:复合物:COMPOUND,4:设备或网关:DEVICE_GATEWAY,5:设备或网关或复合物:DEVICE_GATEWAY_COMPOUND#')
    use_scope_desc = Column(String(64), nullable=False, comment='#使用范围描述#')
    method_desc = Column(String(1024), nullable=False, server_default=text("''"), comment='#函数说明#')
    method_logic = Column(String(512), nullable=False, comment='#函数逻辑#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingTemplateModel(Base):
    __tablename__ = 'b_thing_template_model'
    __table_args__ = {'comment': '物模型模版表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    name = Column(String(100), nullable=False, comment='#模型名称#')
    model_type = Column(TINYINT(4), server_default=text("'1'"), comment='#模型类型#ENUM#1:设备:DEVICE,2:网关:GATEWAY,3:复合物:COMPOUND#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DATETIME(fsp=3), comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DATETIME(fsp=3), comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingTemplateModelAlarm(Base):
    __tablename__ = 'b_thing_template_model_alarm'
    __table_args__ = {'comment': '物模型报警模版表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_template_model.id#')
    name = Column(String(100), nullable=False, comment='#报警名称#')
    alarm_id = Column(String(100), nullable=False, comment='#报警ID#')
    description = Column(String(500), comment='#描述#')
    alarm_level_type = Column(TINYINT(4), server_default=text("'4'"), comment='#报警级别类型#ENUM#1:紧急:URGENCY,2:重要:IMPORTANT,3:警告:WARNING,4:一般:GENERAL,5:不确定:UNSURE#')
    label = Column(String(255), comment='#报警标签#数组字符串#')
    trigger_rule_json = Column(Text, comment='#设置报警触发规则json字符串#')
    property_id = Column(String(255), comment='#与报警同时上报的属性id数组#')
    reason = Column(Text, comment='#原因/解决方案#')
    input_out = Column(TINYINT(4), comment='#输入带出#ENUM#1:输入:input,2:带出:out,3:输入带出:input_out#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingTemplateModelInstruction(Base):
    __tablename__ = 'b_thing_template_model_instruction'
    __table_args__ = {'comment': '物模型指令模版表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_template_model.id#')
    name = Column(String(100), nullable=False, comment='#指令名称#')
    instruction_id = Column(String(100), nullable=False, comment='#指令ID#')
    time_out = Column(INTEGER(11), server_default=text("'0'"), comment='#命令超时时间(秒)#')
    controlled_property = Column(Text, comment='#受控属性#数组字符串#')
    description = Column(String(500), comment='#描述#')
    input_out = Column(TINYINT(4), comment='#输入带出#ENUM#1:输入:input,2:带出:out,3:输入带出:input_out#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BThingTemplateModelProperty(Base):
    __tablename__ = 'b_thing_template_model_property'
    __table_args__ = {'comment': '物模型属性模版表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    model_id = Column(BIGINT(20), nullable=False, comment='#物模型id#REF#b_thing_template_model.id#')
    name = Column(String(100), nullable=False, comment='#属性名称#')
    property_id = Column(String(100), nullable=False, comment='#属性ID#')
    data_type = Column(TINYINT(4), server_default=text("'1'"), comment='#数据类型#ENUM#1:String,2:Number,3:Boolean,4:Integer,5:Binary,6:Json#')
    read_write_type = Column(TINYINT(4), server_default=text("'1'"), comment='#读写类型#ENUM#1:读写:READ_WRITE,2:只读:ONLY_READ,3:只写:ONLY_READ#')
    minimum = Column(String(100), comment='#取值范围#最小值#')
    maximum = Column(String(100), comment='#取值范围#最大值#')
    source_type = Column(TINYINT(4), server_default=text("'1'"), comment='#属性值来源类型#ENUM#1:连接变量:LINK_VARIABLE,2:规则指定:RULES_SPECIFY,3:手动写值:WRITE_VALUE#')
    source_json = Column(Text, comment='#属性值来源json字符串#')
    digits_type = Column(TINYINT(4), server_default=text("'1'"), comment='#小数点保留位数类型#ENUM#1:0位:ZERO,2:1位:ONE,3:2位:TWO,4:3位:THREE,5:4位:FOUR,6:5位:FIVE#')
    save_type = Column(TINYINT(4), server_default=text("'1'"), comment='#历史数据保存方式类型#ENUM#1:上报保存:REPORT,2:周期保存:PERIOD,3:变化保存:CHANGE,4:全部保存:ALL,5:不保存:NO#')
    unit = Column(String(100), comment='#工程单位#')
    label = Column(String(255), comment='#属性标签#数组字符串#')
    input_out = Column(TINYINT(4), comment='#输入带出#ENUM#1:输入:input,2:带出:out,3:输入带出:input_out#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class FlywaySchemaHistory(Base):
    __tablename__ = 'flyway_schema_history'

    installed_rank = Column(INTEGER(11), primary_key=True)
    version = Column(String(50))
    description = Column(String(200), nullable=False)
    type = Column(String(20), nullable=False)
    script = Column(String(1000), nullable=False)
    checksum = Column(INTEGER(11))
    installed_by = Column(String(100), nullable=False)
    installed_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    execution_time = Column(INTEGER(11), nullable=False)
    success = Column(TINYINT(1), nullable=False, index=True)


class LeafAlloc(Base):
    __tablename__ = 'leaf_alloc'

    biz_tag = Column(String(128), primary_key=True, server_default=text("''"))
    max_id = Column(BIGINT(20), nullable=False, server_default=text("'1'"))
    step = Column(INTEGER(11), nullable=False)
    description = Column(String(256))
    update_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class QRTZTRIGGER(Base):
    __tablename__ = 'QRTZ_TRIGGERS'
    __table_args__ = (
        ForeignKeyConstraint(['SCHED_NAME', 'JOB_NAME', 'JOB_GROUP'], ['QRTZ_JOB_DETAILS.SCHED_NAME', 'QRTZ_JOB_DETAILS.JOB_NAME', 'QRTZ_JOB_DETAILS.JOB_GROUP']),
        Index('IDX_QRTZ_T_NFT_ST_MISFIRE_GRP', 'SCHED_NAME', 'MISFIRE_INSTR', 'NEXT_FIRE_TIME', 'TRIGGER_GROUP', 'TRIGGER_STATE'),
        Index('IDX_QRTZ_T_C', 'SCHED_NAME', 'CALENDAR_NAME'),
        Index('IDX_QRTZ_T_NFT_ST', 'SCHED_NAME', 'TRIGGER_STATE', 'NEXT_FIRE_TIME'),
        Index('IDX_QRTZ_T_NFT_MISFIRE', 'SCHED_NAME', 'MISFIRE_INSTR', 'NEXT_FIRE_TIME'),
        Index('IDX_QRTZ_T_G', 'SCHED_NAME', 'TRIGGER_GROUP'),
        Index('IDX_QRTZ_T_NEXT_FIRE_TIME', 'SCHED_NAME', 'NEXT_FIRE_TIME'),
        Index('IDX_QRTZ_T_NFT_ST_MISFIRE', 'SCHED_NAME', 'MISFIRE_INSTR', 'NEXT_FIRE_TIME', 'TRIGGER_STATE'),
        Index('IDX_QRTZ_T_JG', 'SCHED_NAME', 'JOB_GROUP'),
        Index('IDX_QRTZ_T_STATE', 'SCHED_NAME', 'TRIGGER_STATE'),
        Index('IDX_QRTZ_T_J', 'SCHED_NAME', 'JOB_NAME', 'JOB_GROUP'),
        Index('IDX_QRTZ_T_N_STATE', 'SCHED_NAME', 'TRIGGER_NAME', 'TRIGGER_GROUP', 'TRIGGER_STATE'),
        Index('IDX_QRTZ_T_N_G_STATE', 'SCHED_NAME', 'TRIGGER_GROUP', 'TRIGGER_STATE')
    )

    SCHED_NAME = Column(String(120), primary_key=True, nullable=False)
    TRIGGER_NAME = Column(String(190), primary_key=True, nullable=False)
    TRIGGER_GROUP = Column(String(190), primary_key=True, nullable=False)
    JOB_NAME = Column(String(190), nullable=False)
    JOB_GROUP = Column(String(190), nullable=False)
    DESCRIPTION = Column(String(250))
    NEXT_FIRE_TIME = Column(BIGINT(13))
    PREV_FIRE_TIME = Column(BIGINT(13))
    PRIORITY = Column(INTEGER(11))
    TRIGGER_STATE = Column(String(16), nullable=False)
    TRIGGER_TYPE = Column(String(8), nullable=False)
    START_TIME = Column(BIGINT(13), nullable=False)
    END_TIME = Column(BIGINT(13))
    CALENDAR_NAME = Column(String(190))
    MISFIRE_INSTR = Column(SMALLINT(2))
    JOB_DATA = Column(LargeBinary)

    QRTZ_JOB_DETAIL = relationship('QRTZJOBDETAIL')


class QRTZBLOBTRIGGER(QRTZTRIGGER):
    __tablename__ = 'QRTZ_BLOB_TRIGGERS'
    __table_args__ = (
        ForeignKeyConstraint(['SCHED_NAME', 'TRIGGER_NAME', 'TRIGGER_GROUP'], ['QRTZ_TRIGGERS.SCHED_NAME', 'QRTZ_TRIGGERS.TRIGGER_NAME', 'QRTZ_TRIGGERS.TRIGGER_GROUP']),
        Index('SCHED_NAME', 'SCHED_NAME', 'TRIGGER_NAME', 'TRIGGER_GROUP')
    )

    SCHED_NAME = Column(String(120), primary_key=True, nullable=False)
    TRIGGER_NAME = Column(String(190), primary_key=True, nullable=False)
    TRIGGER_GROUP = Column(String(190), primary_key=True, nullable=False)
    BLOB_DATA = Column(LargeBinary)


class QRTZCRONTRIGGER(QRTZTRIGGER):
    __tablename__ = 'QRTZ_CRON_TRIGGERS'
    __table_args__ = (
        ForeignKeyConstraint(['SCHED_NAME', 'TRIGGER_NAME', 'TRIGGER_GROUP'], ['QRTZ_TRIGGERS.SCHED_NAME', 'QRTZ_TRIGGERS.TRIGGER_NAME', 'QRTZ_TRIGGERS.TRIGGER_GROUP']),
    )

    SCHED_NAME = Column(String(120), primary_key=True, nullable=False)
    TRIGGER_NAME = Column(String(190), primary_key=True, nullable=False)
    TRIGGER_GROUP = Column(String(190), primary_key=True, nullable=False)
    CRON_EXPRESSION = Column(String(120), nullable=False)
    TIME_ZONE_ID = Column(String(80))


class QRTZSIMPLETRIGGER(QRTZTRIGGER):
    __tablename__ = 'QRTZ_SIMPLE_TRIGGERS'
    __table_args__ = (
        ForeignKeyConstraint(['SCHED_NAME', 'TRIGGER_NAME', 'TRIGGER_GROUP'], ['QRTZ_TRIGGERS.SCHED_NAME', 'QRTZ_TRIGGERS.TRIGGER_NAME', 'QRTZ_TRIGGERS.TRIGGER_GROUP']),
    )

    SCHED_NAME = Column(String(120), primary_key=True, nullable=False)
    TRIGGER_NAME = Column(String(190), primary_key=True, nullable=False)
    TRIGGER_GROUP = Column(String(190), primary_key=True, nullable=False)
    REPEAT_COUNT = Column(BIGINT(7), nullable=False)
    REPEAT_INTERVAL = Column(BIGINT(12), nullable=False)
    TIMES_TRIGGERED = Column(BIGINT(10), nullable=False)


class QRTZSIMPROPTRIGGER(QRTZTRIGGER):
    __tablename__ = 'QRTZ_SIMPROP_TRIGGERS'
    __table_args__ = (
        ForeignKeyConstraint(['SCHED_NAME', 'TRIGGER_NAME', 'TRIGGER_GROUP'], ['QRTZ_TRIGGERS.SCHED_NAME', 'QRTZ_TRIGGERS.TRIGGER_NAME', 'QRTZ_TRIGGERS.TRIGGER_GROUP']),
    )

    SCHED_NAME = Column(String(120), primary_key=True, nullable=False)
    TRIGGER_NAME = Column(String(190), primary_key=True, nullable=False)
    TRIGGER_GROUP = Column(String(190), primary_key=True, nullable=False)
    STR_PROP_1 = Column(String(512))
    STR_PROP_2 = Column(String(512))
    STR_PROP_3 = Column(String(512))
    INT_PROP_1 = Column(INTEGER(11))
    INT_PROP_2 = Column(INTEGER(11))
    LONG_PROP_1 = Column(BIGINT(20))
    LONG_PROP_2 = Column(BIGINT(20))
    DEC_PROP_1 = Column(DECIMAL(13, 4))
    DEC_PROP_2 = Column(DECIMAL(13, 4))
    BOOL_PROP_1 = Column(String(1))
    BOOL_PROP_2 = Column(String(1))
