'''
Created on 03-Nov-2017

@author: karthikeyan
'''
from flask import Flask
from flask import jsonify
from com.mycompany.service.report_service import ReportService

app = Flask("SystemAnalyzer")

# @app.route("/")
# def redirector():
#     render_template('index.html')


@app.route("/report/cpu")
def get_cpu_report():
    reportService = ReportService()
    return jsonify(reportService.get_all_cpu_report())


@app.route("/report/virtualmemory")
def get_virtual_memory_report():
    reportService = ReportService()
#     return json.dumps(reportService.get_all_ram_report().__dict__)
    return jsonify(reportService.get_all_ram_report())


def start_flask():
    app.run()
