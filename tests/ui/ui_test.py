import os
import csv
import json

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PyQt5.QtCore import Qt

from src.calculator.ui import Calculator


TEST_CASES_FILE = os.path.join(
        os.path.dirname(__file__),
        "ui_test_cases.csv",
)


@pytest.fixture
def calculator(qtbot):
        window = Calculator()
        qtbot.addWidget(window)
        window.show()
        return window


def click_buttons(qtbot, calculator, sequence):
        for label in sequence:
                qtbot.mouseClick(calculator.buttons[label], Qt.LeftButton)


def get_test_cases(source_file: str) -> list:
        test_cases = []
        with open(source_file, newline="", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                        sequence = json.loads(row["sequence"])
                        expected = row["expected"]
                        test_cases.append((sequence, expected))
        return test_cases


@pytest.mark.test_ui
@pytest.mark.parametrize(
        "sequence, expected",
        get_test_cases(TEST_CASES_FILE),
)
def test_ui(qtbot, calculator, sequence, expected):
        click_buttons(qtbot, calculator, sequence)

        assert calculator.display.text() == expected
