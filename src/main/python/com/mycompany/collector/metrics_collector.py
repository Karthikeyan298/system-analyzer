'''
Created on 03-Nov-2017

@author: karthikeyan
'''
import psutil
import datetime
import time
from com.mycompany.entities.report_data import ReportData
from com.mycompany.service.report_service import ReportService


class MetricsCollector(object):

    ram_report_data = None
    cpu_report_data = None

    def get_cpu_metrics(self):
        self.cpu_report_data = ReportData()
        self.cpu_report_data.set_component("CPU")
        self.cpu_report_data.set_usage(psutil.cpu_percent(interval=1))
        self.cpu_report_data.set_time(str(datetime.datetime.now()))
        return self.cpu_report_data

    def get_ram_metrics(self):
        self.ram_report_data = ReportData()
        self.ram_report_data.set_component("VirtualMemory")
        self.ram_report_data.set_usage(psutil.virtual_memory().percent)
        self.ram_report_data.set_time(str(datetime.datetime.now()))
        return self.ram_report_data

    def do_collect_metrics(self):  # pragma: no cover
        while True:  # pragma: no cover
            self.get_cpu_metrics()  # pragma: no cover
            self.get_ram_metrics()  # pragma: no cover
            report_service = ReportService()  # pragma: no cover
            report_service.create_report(self.cpu_report_data)  # pragma: no cover
            report_service.create_report(self.ram_report_data)  # pragma: no cover
            time.sleep(10)


if __name__ == '__main__':  # pragma: no cover
    collector = MetricsCollector()  # pragma: no cover
    collector.do_collect_metrics()  # pragma: no cover
