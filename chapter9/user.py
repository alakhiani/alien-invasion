"""This module offers classes related to defining regular users and admin users"""

class Privileges:
    """Class that represents the privileges the admin user can have"""

    def __init__(self, *privileges) -> None:
        self.privileges = []
        self.set_privileges(*privileges)

    def set_privileges(self, *privileges) -> None:
        self.privileges.extend(privileges)

    def show_privileges(self) -> str:
        return f"User has privileges: {self.privileges}"
    

class User:
    """A class that models a user of the system"""
    def __init__(self, first_name: str, last_name: str, **user_info) -> None:
        self.user_info = user_info
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self) -> str:
        return f"First name: {self.first_name}, Last Name: {self.last_name}, Attributes: {self.user_info}"
    
    def greet_user(self) -> str:
        full_name = f"{self.first_name} {self.last_name}"
        self.increment_login_attempts()
        return f"Hello and welcome back {full_name.title()}, you have logged in {self.login_attempts} times in the past."
    
    def increment_login_attempts(self) -> None:
        self.login_attempts += 1

    def reset_login_attempts(self) -> None:
        self.login_attempts = 0


class AdministratorUser(User):
    """Second class representing a super user"""
    def __init__(self, first_name: str, last_name: str, **user_info) -> None:
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges()
