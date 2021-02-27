'''
Created on 03-Nov-2017

@author: karthikeyan
'''
from com.mycompany.dbutil.reports_dbutil import DBUtil
from sqlalchemy.orm import sessionmaker
from com.mycompany.entities.report_data import ReportData


class ReportService(object):

    dbutil = DBUtil()
    engine = dbutil.create_engine()
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    def create_report(self, report_data):
        self.session.add(report_data)
        self.session.commit()

    def get_all_cpu_report(self):
        report_data_as_list = []
        rep_data = ReportData()
        rs = self.session.query(ReportData).filter_by(_ReportData__component='CPU')
        for data in rs:
            report_data_as_list.append(rep_data.make_dump(data))
        return report_data_as_list

    def get_all_ram_report(self):
        report_data_as_list = []
        rep_data = ReportData()
        rs = self.session.query(ReportData).filter_by(_ReportData__component='VirtualMemory')
        for data in rs:
            report_data_as_list.append(rep_data.make_dump(data))
        return report_data_as_list
