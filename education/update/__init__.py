from urllib import parse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from education.tables.devices_models import BDeviceInfo




if __name__ == '__main__':
    pwd = parse.quote_plus("$^s0694sHcv7qZqu796C2SyIUf4s^IcC")
    engine = create_engine('mysql+pymysql://root:{0}@106.55.218.224:13306/education_device'.format(pwd),echo=True)
    print(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    user = BDeviceInfo(id="23234234",name="显示屏DEVICE-182459",brand="JAGUAR/捷豹", model_number="ZLSHI",power="7.5-250KW",net_model_number="ZLSHI",
                       device_serial_num="23223",protocol_name="sdfsd",net_serial_num="sdfsdf",config_time="2021-02-19 18:30:12",net_brand="sdfsd",
                       run_status=0,class_id="1354374485511798785",class_name="234",template_id=6,image_url="234234")
    session.add(user)
    session.commit()
    print(user)
