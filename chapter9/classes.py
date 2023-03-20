
#9-1 Restaurant
print("\n#9-1")

class Restaurant:
    """A class that represents a restaurant"""

    def __init__(self, name: str, cusine: str) -> None:
        self.name = name
        self.cusine = cusine
        self.open = False
        self.members_served = 0

    def describe_restaurant(self) -> str:
        return f"Restaurant {self.name} serves {self.cusine} cusine!. So far this restaurant has served {self.members_served} guests"
    
    def open_restaurant(self) -> None:
        self.open = True
        print(f"Restaurant is open = {self.open}")

    def close_restaurant(self) -> None:
        self.open = False
        print(f"Restaurant is open = {self.open}")

    def increment_members_served(self, increment: int) -> None:
        if(increment >=0 ):
            self.members_served += increment
        else:
            raise ValueError(f"Can't attempt to rollback members served count with a negative input {increment}")
        
    def set_members_served(self, num_members_served: int) -> None:
        if(num_members_served >= 0):
            self.members_served = num_members_served
        else:
            raise ValueError(f"Cannot set a negative number {num_members_served} for members served")

#9-2 Three Restaurants
print("\n#9-2")

restaurant_1 = Restaurant("C&T Wok", "Chinese")
print(f"Restaurant 1: {restaurant_1.describe_restaurant()}")
restaurant_1.open_restaurant()

restaurant_2 = Restaurant("Spice Hut", "Indian Fast Food")
print(f"Restaurant 2: {restaurant_2.describe_restaurant()}")
restaurant_2.close_restaurant()

restaurant_3 = Restaurant("Alpaca", "Peruvian")
print(f"Restaurant 3: {restaurant_3.describe_restaurant()}")
restaurant_3.open_restaurant()


#9-3 Users
print("\n#9-3")

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
    
user_1 = User('Sam', 'Bowels', age=46, country='UK', city='London')
print(user_1.describe_user())
print(user_1.greet_user())

user_2 = User('Samantha', 'Jones', degree='Masters', school='Kings College', occupation='journalist')
print(user_2.describe_user())
print(user_2.greet_user())


#9-4. Number Served
print("\n#9-4")

restaurant_4 = Restaurant('Peacock', 'Indian')
print(restaurant_4.describe_restaurant())
restaurant_4.increment_members_served(5)
print(restaurant_4.describe_restaurant())

restaurant_5 = Restaurant('Chipotle', 'American Mexican')
print(restaurant_5.describe_restaurant())
restaurant_5.set_members_served(15)
print(restaurant_5.describe_restaurant())
restaurant_5.set_members_served(0)
print(restaurant_5.describe_restaurant())
restaurant_5.set_members_served(100)
print(restaurant_5.describe_restaurant())


#9-5 Login Attempts
print("\n#9-5")

user_3 = User('Charles', 'McNee')
print(user_3.greet_user())
print(user_3.greet_user())
print(user_3.greet_user())
print(user_3.greet_user())
print(user_3.greet_user())
print(user_3.greet_user())

print(f'Resetting login attempts for user: {user_3.describe_user()}')
user_3.reset_login_attempts()
print(user_3.greet_user())


#9-6 Ice Cream Stand
print("\n#9-6")

class IceCreamStand(Restaurant):
    """A specialized restaurant that is an ice cream stand"""
    def __init__(self, name: str, cusine: str, *flavors) -> None:
        super().__init__(name, cusine)
        self.flavors = []
        self.add_flavors_served(*flavors)

    def add_flavors_served(self, *flavors) -> None:
        self.flavors.extend(flavors)

    def describe_restaurant(self) -> str:
        return f"This is an ice cream stand named {self.name} that serves {self.cusine} and offers flavors {self.flavors}"

ice_cream_stand = IceCreamStand('Iceskimo', 'Shaved Ice', 'vanilla', 'chocolate')
ice_cream_stand.add_flavors_served('orange', 'mint')
print(f"Ice Cream Stand: {ice_cream_stand.describe_restaurant()}")


#9-7 Admin
print("\n#9-7")

class AdminUser(User):
    """Special admin user class"""
    def __init__(self, first_name: str, last_name: str, **user_info) -> None:
        super().__init__(first_name, last_name, **user_info)
        self.privileges = []

    def set_privileges(self, *privileges) -> None:
        self.privileges.extend(privileges)

    def show_privileges(self) -> str:
        return f"Admin user {self.describe_user()} has privileges: {self.privileges}"
    
user_4 = AdminUser('Admin', 'Administrator', super_user=True)
user_4.set_privileges('can add post', 'can delete post', 'can ban user')
print(user_4.describe_user())
print(user_4.show_privileges())


#9-8 Privileges
print("\n#9-8")

class Privileges:
    """Class that represents the privileges the admin user can have"""

    def __init__(self, *privileges) -> None:
        self.privileges = []
        self.set_privileges(*privileges)

    def set_privileges(self, *privileges) -> None:
        self.privileges.extend(privileges)

    def show_privileges(self) -> str:
        return f"User has privileges: {self.privileges}"
    

class AdministratorUser(User):
    """Second class representing a super user"""
    def __init__(self, first_name: str, last_name: str, **user_info) -> None:
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges()

user_5 = AdministratorUser('Admin', 'Administrator', super_user=True)
user_5.privileges.set_privileges('can add post', 'can delete post', 'can ban user')
print(user_5.describe_user())
print(user_5.privileges.show_privileges())

