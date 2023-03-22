"""Module containing Employee and related classes"""

class Employee:
    """Class representing an employee"""
    def __init__(self, first_name: str, last_name: str, salary: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def increase_salary(self, increment=5000) -> None:
        if increment < 0:
            raise ValueError(f"Increment '{increment}' cannot be negative!")
        self.salary += increment
