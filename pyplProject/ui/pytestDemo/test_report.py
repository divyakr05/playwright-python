import report
import json


def test_report_json():
    report.generate_report()

    with open("report.json") as file:
        data = json.load(file)
        assert type(data) == dict


def test_report_fields():
    report.generate_report()

    with open("report.json") as file:
        data = json.load(file)
        assert "timestamp" in data
        assert "status" in data