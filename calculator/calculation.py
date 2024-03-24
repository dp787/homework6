import logging
from calculator.calculator import Calculator

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log format
    filename='app.log',  # Specify the log file name
    filemode='a'  # Specify the file mode ('a' for append)
)

class Calculation:
    def __init__(self, operation: str, operands: tuple):
        self.operation = operation
        self.operands = operands

    def perform_operation(self) -> float:
        try:
            if self.operation == "add":
                result = Calculator.add(*self.operands)
            elif self.operation == "subtract":
                result = Calculator.subtract(*self.operands)
            elif self.operation == "multiply":
                result = Calculator.multiply(*self.operands)
            elif self.operation == "divide":
                result = Calculator.divide(*self.operands)
            else:
                raise ValueError("Invalid operation.")

            logging.info(f"Performed operation: {self.operation} with operands {self.operands}. Result: {result}")
            return result
        except ZeroDivisionError:
            logging.error("Attempted to divide by zero.")
            raise ZeroDivisionError("Cannot divide by zero.")
        except Exception as e:
            logging.error(f"An error occurred during calculation: {e}")
            raise e

