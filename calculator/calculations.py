from typing import List
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]
        else:
            return None

    @classmethod
    def get_all_calculations(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()
