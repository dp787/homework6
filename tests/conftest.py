"""This module configures pytest to dynamically generate
   tests with random data for arithmetic operations.
   It uses pytest hooks.
"""

from faker import Faker

def generate_test_data(faker, num_records):
    """
    Generates a list of tuples containing test data.

    Args:
        faker: An instance of Faker to generate random data.
        num_records: The number of records to generate.

    Returns:
        A list of tuples, each containing (num1, num2, expected) for testing.
    """
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else 'ValueError'
    }
    data = []
    for _ in range(num_records):
        num1 = faker.random_number(digits=2)
        num2 = faker.random_number(digits=2)
        operation = faker.random_element(elements=tuple(operations.keys()))
        expected = operations[operation](num1, num2)
        data.append((num1, num2, expected))
    return data

def pytest_addoption(parser):
    """Adds a command-line option to pytest that 
    allows specification of the number of records to generate."""
    parser.addoption("--num_records", action="store", default=5, type=int,
                     help="Number of records to generate")

def pytest_generate_tests(metafunc):
    """
    Generates test cases dynamically based on the number 
    of records specified via command-line option.
    This function checks for the presence of a 'dynamic_data' fixture 
    and generates random test data accordingly.
    """
    if "dynamic_data" in metafunc.fixturenames:
        faker = Faker()
        num_records = metafunc.config.option.num_records
        data = generate_test_data(faker, num_records)

        metafunc.parametrize("num1, num2, expected", data)
