#5.1
print("\n#5.1")
car = 'subaru'
print("Is car == 'subaru'? I predicted True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predicted False.")
print(car == 'audi')

print("\n#5.2a")

#5.2
AGE_1 = 18
AGE_2 = 21
my_age = 45
son_age = 6
print("Does my age allow me to drive a car? I predicted True")
print(my_age >= AGE_1)
print("Does my son's age allow him to have a drink?")
print(son_age >= AGE_1 and son_age >= AGE_2)

print("\n#5.2b")

pizza_toppings = ['Pepperoni', 'Pineapple', 'Olives']
desired_topping = 'Pineapple'
print(f"Is {desired_topping} a valid topping? {desired_topping in pizza_toppings}")
desired_topping = 'Peppers'
print(f"Is {desired_topping} a valid topping? {desired_topping in pizza_toppings}")

print("\n#5.2c")

restricted_list = ('AAPL.OQ', 'TSLA.OQ', 'T.N')
stock = 'GE.N'
print(f"Is {stock} permitted to trade? {stock not in restricted_list}")
stock = 'AAPL.OQ'
print(f"Is {stock} permitted to trade? {stock not in restricted_list}")

for stock in restricted_list:
    if stock == 'AAPL.OQ':
        print(stock.lower())
    else:
        print(stock)

print("\n#5.3")

#5.3
LOW_SCORE_COLOR = 'green'
MEDIUM_SCORE_COLOR = 'yellow'
HIGH_SCORE_COLOR = 'red'
alien_color = 'Green'
if alien_color.lower() == LOW_SCORE_COLOR:
    print(f"You just earned 5 points for shooting the {alien_color} alien")

alien_color = 'Red'
if alien_color.lower() == LOW_SCORE_COLOR:
    print(f"You just earned 5 points for shooting the {alien_color} alien")
elif alien_color.lower() == HIGH_SCORE_COLOR:
    print(f"You just earned 2 points for shooting the {alien_color} alien")
else:
    print(f"Missed, better luck next time shooting the {LOW_SCORE_COLOR} alien, you shot {alien_color} alien this time.")

print("\n#5.5")

#5.5
alien_color = 'blue'
score = 0

if alien_color.lower() == HIGH_SCORE_COLOR:
    score = 15
elif alien_color.lower() == MEDIUM_SCORE_COLOR:
    score = 10
elif alien_color.lower() == LOW_SCORE_COLOR:
    score = 5

print(f"You just earned {score} points for shooting the {alien_color} alien")


print("\n5.8")

#5.8
users_list = ['Admin', 'Mark', 'Harry', 'Charles', 'Ryan', 'Smith', 'Jaden']
for user in users_list:
    if user.lower() == 'admin':
        print(f"Hello {user}, would you like to ssee a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

print("\n#5.9")

#5.9
empty_users_list = []
if not empty_users_list:
    print("We need to find some users!")
else:
    print(f"We have {len(empty_users_list)} registered users.")

print("\n#5.10")
#5.10
current_users_loser_case = [user.lower() for user in users_list]
print(f"Currently registered users list in lower case is: {current_users_loser_case}")
new_users = ['JADEN', 'harry', 'John', 'Barry', 'Adminstrator']
for user in new_users:
    if user.lower() in current_users_loser_case:
        print(f"Sorry {user} username is already in use, choose another username!")
    else:
        print(f"{user} is available for registration!")

print ("\n#5.11")
#5.11
numbers_list = list(range(1,10))
suffix = ""
for num in numbers_list:
    if num == 1:
        suffix = "st"
    elif num == 2:
        suffix = "nd"
    elif num == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{num}{suffix}", end=" ")
print()
