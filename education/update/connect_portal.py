from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib import parse
from education.tables.devices_models import BDeviceInfo


class Portal(object):

    session = None
    isClosed = True
    pwd = parse.quote_plus("$^s0694sHcv7qZqu796C2SyIUf4s^IcC")

    def __init__(self):
        url = "mysql+pymysql://root:{0}@106.55.218.224:13306/education_portal".format(self.pwd)
        engine = create_engine(url, convert_unicode=True, echo=False, encoding="utf8")
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.isClosed = False

    def query(self, type):
        query = self.session.query(type)
        return query

    def add(self, item):
        self.session.add(item)

    def add_all(self, items):
        self.session.add_all(items)

    def delete(self, item):
        self.session.delete(item)

    def commit(self):
        self.session.commit()

    def close(self):
        if self.isClosed:
            pass
        self.session.close()
        self.isClosed = True


if __name__ == '__main__':
    a = Portal().query(BDeviceInfo)
    u = a.filter_by(name="显示屏DEVICE-182459").first()
    print(u.name)
