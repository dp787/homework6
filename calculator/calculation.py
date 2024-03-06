from calculator.calculator import Calculator

class Calculation:
    def __init__(self, operation: str, operands: tuple):
        self.operation = operation
        self.operands = operands

    def perform_operation(self) -> float:
        if self.operation == "add":
            return Calculator.add(*self.operands)
        elif self.operation == "subtract":
            return Calculator.subtract(*self.operands)
        elif self.operation == "multiply":
            return Calculator.multiply(*self.operands)
        elif self.operation == "divide":
            return Calculator.divide(*self.operands)
        else:
            raise ValueError("Invalid operation.")
