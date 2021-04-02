# coding: utf-8
from sqlalchemy import Column, DateTime, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BDataDictionary(Base):
    __tablename__ = 'b_data_dictionary'
    __table_args__ = {'comment': '数据字典表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    dict_key = Column(String(50), nullable=False, comment='#数据属性key#')
    dict_value = Column(String(50), nullable=False, comment='#数据属性值value#')
    dict_desc = Column(String(50), nullable=False, comment='#数据类型描述#')
    dict_key_desc = Column(String(255), comment='#业务key描述#')
    order_by = Column(TINYINT(4), comment='#排序#')
    parent_id = Column(BIGINT(20), comment='#父数据id#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BDeviceInfo(Base):
    __tablename__ = 'b_device_info'
    __table_args__ = {'comment': '设备信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    name = Column(String(50), nullable=False, comment='#设备名称#')
    brand = Column(String(50), comment='#品牌#')
    model_number = Column(String(50), comment='#设备型号#')
    power = Column(String(50), comment='#功率#')
    net_model_number = Column(String(50), comment='#网关型号#')
    device_serial_num = Column(String(50), comment='#设备序列号#')
    protocol_name = Column(String(50), comment='#工控协议名称#')
    net_serial_num = Column(String(50), comment='#网关序列号#')
    config_time = Column(DateTime, comment='#配置版本的最新时间#')
    net_brand = Column(String(50), comment='#网关品牌#')
    run_status = Column(TINYINT(4), server_default=text("'0'"), comment='#设备运行状态#ENUM#1:运行;0:停止')
    class_id = Column(BIGINT(20), comment='#班级id#')
    class_name = Column(String(50), comment='#班级名称#')
    template_id = Column(BIGINT(20), comment='#模板id#')
    image_url = Column(String(100), comment='#设备图片url#')
    creator_true_name = Column(String(50), comment='#创建人真实姓名#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    config_version = Column(INTEGER(4), server_default=text("'0'"), comment='#配置版本号#')
    school_id = Column(BIGINT(20), comment='#学校id#')
    start_time = Column(DateTime, comment='#设备最新一次启动时间#')


class BDeviceNConfig(Base):
    __tablename__ = 'b_device_n_config'
    __table_args__ = {'comment': '北向配置信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#南向配置主键id#')
    device_id = Column(BIGINT(20), comment='#设备表id#REF#b_device_info.id')
    server_addr = Column(String(50), comment='#服务器地址#')
    server_port = Column(INTEGER(6), comment='#服务器端口#')
    connect_protocol_value = Column(String(20), comment='#连接协议值#')
    connect_protocol_desc = Column(String(20), comment='#连接协议描述#')
    upload_freq_value = Column(INTEGER(11), comment='#上传频率（秒）#')
    upload_freq_desc = Column(String(50), comment='#上传频率描述#')
    connect_method = Column(String(20), comment='#连接方法#')
    tran_flag = Column(TINYINT(1), comment='#是否数据转义#ENUM#1:是;0:否')
    client_id = Column(String(30), comment='#clientId#')
    user_name = Column(String(64), comment='#用户名#')
    password = Column(String(64), comment='#密码#')
    accept_topic = Column(String(50), comment='#接收topic#')
    send_topic = Column(String(50), comment='#发送topic#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    mobile = Column(String(11), comment='#手机号#')
    machine_id = Column(String(20), comment='#设备ID#')


class BDeviceNPoint(Base):
    __tablename__ = 'b_device_n_point'
    __table_args__ = {'comment': '北向点表信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    device_id = Column(BIGINT(20), comment='#设备id#REF#b_device_info.id')
    n_config_id = Column(BIGINT(20), comment='#北向配置id#REF#b_template_nconfig.id#')
    s_point_id = Column(BIGINT(20), comment='#南向采集点id#')
    name = Column(String(50), comment='#参数名称#')
    unit = Column(String(15), comment='#单位#')
    data_desc = Column(String(100), comment='#数据说明#')
    data_type = Column(String(50), comment='#数据类型名称#')
    register_type = Column(String(25), comment='#寄存器类型名称#')
    register_address = Column(String(20), comment='#寄存器地址#')
    register_offset = Column(INTEGER(4), comment='#寄存器偏移地址#')
    mapping_variable = Column(String(50), comment='#映射变量#')
    read_write_type = Column(TINYINT(4), comment='#读写类型#0:只读:READ-ONLY,1:只写:WRITE-ONLY#')
    rule_type = Column(TINYINT(4), comment='#规则类型#')
    rule_freq_value = Column(INTEGER(11), comment='#规则频率#')
    rule_freq_desc = Column(String(50), comment='#规则频率描述#')
    rule_values = Column(String(250), comment='#规则数据值（一个或多个逗号分隔）#')
    rule_start_value = Column(String(20), comment='#规则数据起始值#')
    system_flag = Column(TINYINT(1), server_default=text("'0'"), comment='#系统参数标志#ENUM#1:系统参数;0:非系统参数#')
    fix_flag = Column(TINYINT(1), comment='#固定采集点#ENUM#1:不可删除;0:可删除#')
    rule_end_value = Column(String(20), comment='#规则数据结束值#')
    rule_step_length = Column(String(20), comment='#规则数据步长#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    type_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#采集点种类标志#ENUM#0:正常;1:急停;2:开关#')


class BDeviceSConfig(Base):
    __tablename__ = 'b_device_s_config'
    __table_args__ = {'comment': '南向配置信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#南向配置主键id#')
    device_id = Column(BIGINT(20), comment='#设备表id#REF#b_device_info.id')
    connect_protocol_value = Column(String(25), comment='#连接协议value#')
    connect_protocol_desc = Column(String(50), comment='#连接协议描述#')
    agreement = Column(String(50), comment='#规约#')
    kind = Column(String(50), comment='#分类#')
    remote_addr = Column(String(50), comment='#远程地址#')
    remote_port = Column(INTEGER(6), comment='#远程端口#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BDeviceSPoint(Base):
    __tablename__ = 'b_device_s_point'
    __table_args__ = {'comment': '南向点表信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    device_id = Column(BIGINT(20), comment='#设备id#')
    s_config_id = Column(BIGINT(20), comment='#南向配置id#REF#b_device_sconfig.id#')
    name = Column(String(50), comment='#参数名称#')
    unit = Column(String(15), comment='#单位#')
    data_desc = Column(String(100), comment='#数据说明#')
    data_type = Column(String(50), comment='#数据类型#')
    register_type = Column(String(25), comment='#寄存器类型名称#')
    register_address = Column(String(20), comment='#寄存器地址#')
    register_offset = Column(INTEGER(4), comment='#寄存器偏移地址#')
    read_write_type = Column(TINYINT(4), comment='#读写类型#0:只读:READ-ONLY,1:只写:WRITE-ONLY#')
    rule_type = Column(TINYINT(4), comment='#规则类型#')
    rule_freq_value = Column(INTEGER(11), comment='#规则频率#')
    rule_freq_desc = Column(String(50), comment='#规则频率描述#')
    rule_values = Column(String(250), comment='#规则数据值（一个或多个逗号分隔）#')
    rule_start_value = Column(String(20), comment='#规则数据起始值#')
    rule_end_value = Column(String(20), comment='#规则数据结束值#')
    rule_step_length = Column(String(20), comment='#规则数据步长#')
    system_flag = Column(TINYINT(1), server_default=text("'0'"), comment='#系统参数标志#ENUM#1:系统参数;0:非系统参数##')
    fix_flag = Column(TINYINT(1), server_default=text("'0'"), comment='#固定采集点#ENUM#1:不可删除;0:可删除#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    type_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#采集点种类标志#ENUM#0:正常;1:急停;2:开关#')


class BTemplateInfo(Base):
    __tablename__ = 'b_template_info'
    __table_args__ = {'comment': '模板信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    name = Column(String(50), nullable=False, comment='#设备名称#')
    brand = Column(String(50), comment='#品牌#')
    model_number = Column(String(50), comment='#设备型号#')
    power = Column(String(50), comment='#功率#')
    voltage = Column(String(25), comment='#电压#')
    device_serial_num = Column(String(50), comment='#设备序列号#')
    default_flag = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='#默认模板#ENUM#1:是;0:否')
    protocol_name = Column(String(50), comment='#工控协议值#')
    net_model_number = Column(String(50), comment='#网关型号#')
    upload_freq_unit = Column(TINYINT(2), comment='#上传频率单位#ENUM#1:秒，2:分钟')
    net_serial_num = Column(String(50), comment='#网关序列号#')
    net_brand = Column(String(50), comment='#网关品牌#')
    image_url = Column(String(100), comment='#模板图片URL#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BTemplateNConfig(Base):
    __tablename__ = 'b_template_n_config'
    __table_args__ = {'comment': '模版北向配置信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#南向配置主键id#')
    template_id = Column(INTEGER(20), comment='#模板id#REF#b_template_info.id')
    server_addr = Column(String(50), comment='#服务器地址#')
    server_port = Column(INTEGER(6), comment='#服务器端口#')
    connect_protocol_value = Column(String(20), comment='#连接协议#')
    connect_protocol_desc = Column(String(20), comment='#连接协议描述#')
    upload_freq_value = Column(INTEGER(11), comment='#上传频率（秒）#')
    upload_freq_desc = Column(String(50), comment='#上传频率描述#')
    connect_method = Column(String(50), comment='#连接方法#')
    tran_flag = Column(TINYINT(1), comment='#是否数据转义#ENUM#1:是;0:否#')
    client_id = Column(String(30), comment='#clientId#')
    user_name = Column(String(64), comment='#用户名#')
    password = Column(String(64), comment='#密码#')
    accept_topic = Column(String(50), comment='#接收topic#')
    send_topic = Column(String(50), comment='#发送topic#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    mobile = Column(String(11), comment='#手机号#')
    machine_id = Column(String(20), comment='#设备ID#')


class BTemplateNPoint(Base):
    __tablename__ = 'b_template_n_point'
    __table_args__ = {'comment': '北向点表信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    template_id = Column(BIGINT(20), comment='#模板id#REF#b_template_info.id')
    n_config_id = Column(BIGINT(20), comment='#北向配置id#REF#b_template_nconfig.id#')
    name = Column(String(50), comment='#参数名称#')
    unit = Column(String(15), comment='#单位#')
    data_desc = Column(String(100), comment='#数据说明#')
    data_type = Column(String(50), comment='#数据类型名称#')
    register_type = Column(String(25), comment='#寄存器类型名称#')
    register_address = Column(String(20), comment='#寄存器地址#')
    register_offset = Column(INTEGER(4), comment='#寄存器偏移地址#')
    mapping_variable = Column(String(50), comment='#映射变量#')
    read_write_type = Column(TINYINT(4), comment='#读写类型#0:只读:READ-ONLY,1:只写:WRITE-ONLY#')
    rule_type = Column(TINYINT(4), comment='#规则类型#')
    rule_freq_value = Column(INTEGER(11), comment='#规则频率#')
    rule_freq_desc = Column(String(50), comment='#规则频率描述#')
    rule_values = Column(String(250), comment='#规则数据值（一个或多个逗号分隔）#')
    rule_start_value = Column(String(20), comment='#规则数据起始值#')
    rule_end_value = Column(String(20), comment='#规则数据结束值#')
    rule_step_length = Column(String(20), comment='#规则数据步长#')
    fix_flag = Column(TINYINT(1), server_default=text("'1'"), comment='#固定采集点#ENUM#1:不可删除;0:可删除##')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    type_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#采集点种类标志#ENUM#0:正常;1:急停;2:开关#')


class BTemplateSConfig(Base):
    __tablename__ = 'b_template_s_config'
    __table_args__ = {'comment': '模版南向配置信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#南向配置主键id#')
    template_id = Column(INTEGER(22), comment='#模板id#REF#b_template_info.id')
    connect_protocol_value = Column(String(25), comment='#连接协议value#')
    connect_protocol_desc = Column(String(50), comment='#连接协议描述#')
    agreement = Column(String(50), comment='#规约#')
    kind = Column(String(50), comment='#分类#')
    remote_addr = Column(String(50), comment='#远程地址#')
    remote_port = Column(INTEGER(6), comment='#远程端口#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BTemplateSPoint(Base):
    __tablename__ = 'b_template_s_point'
    __table_args__ = {'comment': '南向点表信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    template_id = Column(BIGINT(20), comment='#模板id#REF#b_template_info.id')
    s_config_id = Column(BIGINT(20), comment='#南向配置id#REF#b_template_sconfig.id#')
    name = Column(String(50), comment='#参数名称#')
    unit = Column(String(15), comment='#单位#')
    data_desc = Column(String(100), comment='#数据说明#')
    data_type = Column(String(50), comment='#数据类型#')
    register_type = Column(String(25), comment='#寄存器类型名称#')
    register_address = Column(String(20), comment='#寄存器地址#')
    register_offset = Column(INTEGER(4), comment='#寄存器偏移地址#')
    read_write_type = Column(TINYINT(4), comment='#读写类型#0:只读:READ-ONLY,1:只写:WRITE-ONLY#')
    rule_type = Column(TINYINT(4), comment='#规则类型#')
    rule_freq_value = Column(INTEGER(11), comment='#规则频率#')
    rule_freq_desc = Column(String(50), comment='#频率描述#')
    rule_values = Column(String(250), comment='#规则数据值（一个或多个逗号分隔）#')
    rule_start_value = Column(String(20), comment='#规则数据起始值#')
    rule_end_value = Column(String(20), comment='#规则数据结束值#')
    rule_step_length = Column(String(20), comment='#规则数据步长#')
    fix_flag = Column(TINYINT(1), server_default=text("'1'"), comment='#固定采集点#ENUM#1:不可删除;0:可删除#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    type_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#采集点种类标志#ENUM#0:正常;1:急停;2:开关#')


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
