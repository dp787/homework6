import logging
from typing import List
from calculator.calculation import Calculation

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log format
    filename='app.log',  # Specify the log file name
    filemode='a'  # Specify the file mode ('a' for append)
)

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        cls.history.append(calculation)
        logging.info(f"Added calculation to history: {calculation.operation} with operands {calculation.operands}.")

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        if cls.history:
            last_calculation = cls.history[-1]
            logging.info(f"Retrieved last calculation from history: {last_calculation.operation} with operands {last_calculation.operands}.")
            return last_calculation
        else:
            logging.warning("Attempted to retrieve last calculation from empty history.")
            return None

    @classmethod
    def get_all_calculations(cls) -> List[Calculation]:
        logging.info("Retrieved all calculations from history.")
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()
        logging.info("Cleared calculation history.")

