import logging

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log format
    filename='app.log',  # Specify the log file name
    filemode='a'  # Specify the file mode ('a' for append)
)

class Calculator:
    commands = {
        'add': 'Addition',
        'subtract': 'Subtraction',
        'multiply': 'Multiplication',
        'divide': 'Division',
        'menu': 'Display Menu',
    }

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        logging.info(f"Performed addition: {a} + {b} = {result}")
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        logging.info(f"Performed subtraction: {a} - {b} = {result}")
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        logging.info(f"Performed multiplication: {a} * {b} = {result}")
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            logging.error("Attempted to divide by zero.")
            raise ValueError("Cannot divide by zero.")
        result = a / b
        logging.info(f"Performed division: {a} / {b} = {result}")
        return result

    @classmethod
    def display_menu(cls):
        logging.info("Displayed menu.")
        print("Available Commands:")
        for command, description in cls.commands.items():
            print(f"{command}: {description}")

    @classmethod
    def execute_command(cls, command):
        if command not in cls.commands:
            logging.error(f"Invalid command: {command}")
            raise ValueError("Invalid command")

        if command == 'add':
            return cls.add(2, 3)
        elif command == 'subtract':
            return cls.subtract(5, 3)
        elif command == 'multiply':
            return cls.multiply(2, 3)
        elif command == 'divide':
            return cls.divide(6, 2)
        elif command == 'menu':
            cls.display_menu()
        else:
            logging.error(f"Invalid command: {command}")
            raise ValueError("Invalid command")
