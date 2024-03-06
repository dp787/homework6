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
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @classmethod
    def display_menu(cls):
        print("Available Commands:")
        for command, description in cls.commands.items():
            print(f"{command}: {description}")

    @classmethod
    def execute_command(cls, command):
        if command not in cls.commands:
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
            raise ValueError("Invalid command")
