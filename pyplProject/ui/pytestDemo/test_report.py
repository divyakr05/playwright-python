import pytest
import report
import json


# Fixtures --> used for Initialization - setup services, state, or other operating environments
# These are accessed by test functions through arguments
# By default the scope is function, ie. fixture gets run when function is called
# scope can be module, whole test session
@pytest.fixture()
def report_json():
    print("\n[ Fixture ]: .......return report data")
    report.generate_report()

    with open("C:/Users/divyar/PycharmProjects/pyplProject/.venv/report.json") as file:
        return json.load(file)


def test_report_json(report_json):
    print("[ Test ]: received -", report_json)
    assert type(report_json) == dict


def test_report_fields(report_json):
    print("[ Test ]: received -", report_json)
    assert "timestamp" in report_json
    assert "status" in report_json
