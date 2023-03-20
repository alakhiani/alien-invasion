#9-11
from user import User, AdministratorUser

user_1 = User('John', 'Doe', age=35, city='Langdon', state='VA', status='Active')
print(user_1.describe_user())

user_2 = AdministratorUser('Admin', 'Administrator', super_user=True)
user_2.increment_login_attempts()
user_2.privileges.set_privileges('can add post', 'can delete post', 'can delete user')
print(user_2.describe_user())
print(user_2.privileges.show_privileges())
