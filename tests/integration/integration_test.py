import pytest
import os
import csv
import json
import logging

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt5.QtWidgets import QApplication
from src.calculator.ui import Calculator


logger = logging.getLogger(__name__)

TEST_CASES_FILE = os.path.join(
        os.path.dirname(__file__),
        "integration_test_cases.csv",
)


@pytest.fixture
def calculator():
        app = QApplication.instance() or QApplication([])
        window = Calculator()
        yield window
        window.close()
        app.processEvents()


def press_sequence(calculator, sequence):
        for value in sequence:
                calculator.button_clicked(value)


def get_test_cases(source_file: str) -> list:
        test_cases = []
        with open(source_file, newline="", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                        sequence = json.loads(row["sequence"])
                        expected = row["expected"]
                        test_cases.append((sequence, expected))
        return test_cases


@pytest.mark.test_button_clicked
@pytest.mark.parametrize(
        "sequence, expected",
        get_test_cases(TEST_CASES_FILE)
)
def test_button_clicked(calculator, sequence, expected) -> None:
        press_sequence(calculator, sequence)
        actual_value = calculator.display.text()
        logger.info(
                "sequence=%s actual=%s expected=%s",
                sequence,
                actual_value,
                expected,
        )

        assert actual_value == expected
