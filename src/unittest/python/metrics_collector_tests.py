'''
Created on 08-Nov-2017

@author: user
'''
import unittest
from com.mycompany.collector.metrics_collector import MetricsCollector


class MetricsCollectorTests(unittest.TestCase):

    def setUp(self):
        self.collector = MetricsCollector()
        
    def test_get_cpu_report(self):
        cpu_report_data = self.collector.get_cpu_metrics()
        self.assertEqual(str, type(cpu_report_data.get_component())) 
        self.assertEqual(float, type(cpu_report_data.get_usage()))
        self.assertEqual(str, type(cpu_report_data.get_time())) 

    def test_get_ram_report(self):
        ram_report_data = self.collector.get_ram_metrics()
        self.assertEqual(str, type(ram_report_data.get_component())) 
        self.assertEqual(float, type(ram_report_data.get_usage()))
        self.assertEqual(str, type(ram_report_data.get_time()))
        
#     @patch.object(ReportService, "create_cpu_report") 
#     @patch.object(ReportService, "create_ram_report")
#     @pytest.mark.timeout(2)  
#     def test_do_collect_metrics(self, mock_create_cpu_report, mock_create_ram_report):
# #         self.collector.do_collect_metrics()
# #         self.assertEqual(str, type(self.collector.cpu_report_data.get_component()))
# #         self.assertEqual(float, type(self.collector.cpu_report_data.get_usage()))
# #         self.assertEqual(str, type(self.collector.cpu_report_data.get_time()))
#         time.sleep(20)
        
        