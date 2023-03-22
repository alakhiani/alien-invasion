import pytest
from employee import Employee

@pytest.fixture
def employee() -> Employee:
    """An employee object that will be available to all test functions"""
    return Employee('John', 'Doe', 50000)

def test_give_default_raise(employee) -> None:
    employee.increase_salary()
    assert employee.salary == 55000

def test_give_custom_raise(employee) -> None:
    employee.increase_salary(10000)
    assert employee.salary == 60000
