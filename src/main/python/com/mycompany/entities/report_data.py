from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float

Base = declarative_base()


class ReportData(Base):
    __tablename__ = 'report_data'
    __component = Column(String(50), primary_key=True)
    __usage = Column(Float(4, 2))
    __time = Column(String(50), primary_key=True)

    def set_component(self, component):
        self.__component = component

    def set_usage(self, usage):
        self.__usage = usage

    def set_time(self, time):
        self.__time = time

    def get_component(self):
        return self.__component

    def get_usage(self):
        return self.__usage

    def get_time(self):
        return self.__time

    def make_dump(self, rep_data):
        data = {
                'component': rep_data.get_component(),
                'usage': float(rep_data.get_usage()),
                'time': rep_data.get_time(),
                }
        return data
