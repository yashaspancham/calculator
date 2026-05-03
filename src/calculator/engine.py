import math
import re


def calculate_expression(expression):
        try:
                expression = expression.replace("×", "*")
                expression = expression.replace("÷", "/")
                expression = expression.replace("−", "-")
                expression = expression.strip()

                expression = _handle_percentage(expression)

                result = eval(expression)

                if isinstance(result, float) and result.is_integer():
                        result = int(result)

                return result

        except Exception:
                return "Error"


def _handle_percentage(expression):
        if "%" not in expression:
                return expression

        match = re.search(r'^(.*?)([+\-])(\d+\.?\d*)%$', expression)
        if match:
                base_expr = match.group(1)
                op = match.group(2)
                percent_num = match.group(3)
                return f"{base_expr}{op}({base_expr})*{percent_num}/100"

        return expression.replace("%", "/100")


def extract_last_number(expression):
        match = re.search(r'^(.*[+\-×÷%])?(\d+\.?\d*)$', expression)
        if match:
                prefix = match.group(1) or ""
                number = match.group(2)
                return prefix, number
        return "", expression


def square_root(value):
        try:
                n = float(value)
                if n < 0:
                        return "Error"
                result = math.sqrt(n)
                if result.is_integer():
                        return int(result)
                return result
        except Exception:
                return "Error"


def square(value):
        try:
                n = float(value)
                result = n ** 2
                if isinstance(result, float) and result.is_integer():
                        return int(result)
                return result
        except Exception:
                return "Error"


def negate(value):
        try:
                n = float(value)
                result = -n
                if isinstance(result, float) and result.is_integer():
                        return int(result)
                return result
        except Exception:
                return "Error"