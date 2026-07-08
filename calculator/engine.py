class CalculatorEngine:

    @staticmethod
    def calculate(expression):

        if expression.strip() == "":
            return ""

        try:
            result = eval(expression)

            if isinstance(result, float):
                result = round(result, 10)

                if result.is_integer():
                    result = int(result)

            return str(result)

        except ZeroDivisionError:
            return "Cannot divide by zero"

        except Exception:
            return "Error"