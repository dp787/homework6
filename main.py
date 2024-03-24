import sys
import logging
from calculator.calculator import Calculator

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log format
    filename='app.log',  # Specify the log file name
    filemode='w'  # Specify the file mode ('w' for write)
)

def perform_operation(op, num1, num2):
    """Performs a calculation based on the operation provided."""
    operations = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    if op in operations:
        return operations[op](num1, num2)
    else:
        raise ValueError(f"Unknown operation: {op}")

def parse_and_validate_numbers(num1, num2):
    """Attempts to convert inputs to floats and validates them."""
    try:
        num1 = float(num1)
        num2 = float(num2)
        return num1, num2
    except ValueError:
        logging.error(f"Invalid number input: {num1} or {num2} is not a valid number.")
        raise ValueError(f"Invalid number input: {num1} or {num2} is not a valid number.")

def main():
    if len(sys.argv) < 4:
        logging.error("Not enough arguments provided.")
        print("Usage: python main.py <number1> <number2> <operation>")
        print("Operations are 'add', 'subtract', 'multiply', 'divide'")
        return

    _, arg_num1, arg_num2, operation = sys.argv

    try:
        num1, num2 = parse_and_validate_numbers(arg_num1, arg_num2)
        result = perform_operation(operation, num1, num2)
        logging.info(f"Performed operation: {num1} {operation} {num2} = {result}")
        print(f"The result of {num1} {operation} {num2} is equal to {result}")
    except ValueError as e:
        logging.error(str(e))
        print(e)

if __name__ == "__main__":
    main()
