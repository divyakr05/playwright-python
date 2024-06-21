import json


def generate_report():
    # generate report data
    data = {
        "timestamp": "2023-4-27 12-37-9",
        "status": "PASSED",
        "summary": "module.py::test_case"
    }
    # open json file
    # in writing mode
    with open("C:/Users/divyar/PycharmProjects/pyplProject/.venv/report.json", "w") as file:
        # write data to json file
        json.dump(data, file)