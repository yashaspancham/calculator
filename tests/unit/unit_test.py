import pytest
import logging
import pandas
from src.calculator.engine import calculate_expression, square_root
from src.calculator.engine import (
        calculate_expression,
        square_root,
        square,
        negate,
        extract_last_number,
        _handle_percentage
)

FUNCTION_MAP = {
        "calculate_expression": calculate_expression,
        "square_root": square_root,
        "square": square,
        "negate": negate,
        "extract_last_number": extract_last_number,
        "handle_percentage":_handle_percentage
}


logger = logging.getLogger(__name__)

def get_test_cases(source_file: str) -> list:
        excel_engines = {
                "xlsx": "openpyxl",
                "xls": "xlrd",
                "ods": "odf",
                "xlsb": "pyxlsb"
        }
        if source_file.split(".")[-1] == "csv":
                data_frame = pandas.read_csv(source_file)
        else:
                data_frame = pandas.read_excel(source_file, engine=excel_engines[source_file.split(".")[-1]])
        # data_frame = data_frame.iloc[:, 1:]
        print(data_frame)
        return list(data_frame.itertuples(index=False, name=None))




@pytest.mark.test_calculate_expression
@pytest.mark.parametrize('function, function_input, expected_output', get_test_cases("./tests/unit/unit_test_cases.csv"))
def test_calculate_expression(function, function_input: str, expected_output: int|float|str) -> None:
        logger.info(f"function: {function}")
        logger.info(f"function_input: {function_input}")
        actual_value = FUNCTION_MAP[function](function_input)
        logger.info(f"actual: {actual_value}")
        logger.info(f"expected: {expected_output}")
        assert str(actual_value) == str(expected_output)



