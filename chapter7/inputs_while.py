#7-1
print("\n7-1")
# car = input("What kind of car would you like to rent?: ")
car = 'BMW' # uncomment above line to capture actual user input
print(f"Let met see if I can find you a {car}")

#7-2
print("\n#7-2")
#num_of_guests = input("How many people are in your dinner group please? ")
num_of_guests = 5 # uncomment above line to capture actual user input
count_of_guests = int(num_of_guests)
if count_of_guests > 8:
    print("Sorry, you will have to wait for a table")
elif count_of_guests > 0:
    print("Your table is ready")
else:
    print(f"Invalid number of guests {count_of_guests}")


#7-3
print("\n#7-3")
#number = input("Please enter a number: ")
number = '5' # uncomment above line to capture actual user input
num = int(number)
if num != 0 and num % 10 == 0:
    print(f"{num} is a multiple of 10")
else:
    print(f"{num} is not a multple of 10")


#7-4
print("\n#7-4")

topping = ''
while topping != 'done':
    # topping = input("Which topping would you like on your pizza? Type 'done' to complete your toppings entry. ")
    topping = 'done' # uncomment above line to capture actual user input

    if topping != 'done':
        print(f"I'll add {topping} to your pizza")


#7-5
print("\n#7-5")

age = 0

while age >=0:
    # age_entry = input("Enter your age to find out what the cost of the movie ticket is, use <0 to quit: ")
    age_entry = -1 # uncomment above line to capture actual user input
    age = int(age_entry)
    price = 0.0;
    if age < 0:
        break
    elif age > 3 and age <= 12:
        price = 10.0
    elif age > 12:
        price = 15.0

    print(f"Your price is {price}")


#7-6
print("\n#7-6")

age = 0
loop_tries = 5

while age >=0 and loop_tries > 0:
    # age_entry = input("Enter your age to find out what the cost of the movie ticket is, use <0 to quit: ")
    age_entry = -1 # uncomment above line to capture actual user input
    age = int(age_entry)
    price = 0.0;
    if age < 0:
        break
    elif age > 3 and age <= 12:
        price = 10.0
    elif age > 12:
        price = 15.0

    print(f"Your price is {price}")
    loop_tries -= 1


#7-8
print("\n#7-8")

sandwich_orders = ['cheese', 'pastrami', 'turkey', 'chicken', 'smoked salmon']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made you a {sandwich} sandwich!")
    finished_sandwiches.insert(0, sandwich)

print(f"Here are all the sandwiches I made today {finished_sandwiches}")

#7-9
print("\n#7-9")

sandwich_orders.clear()
sandwich_orders = ['cheese', 'pastrami', 'turkey', 'chicken', 'smoked salmon', 'pastrami', 'cheese', 'pastrami', 'pastrami']
finished_sandwiches.clear()

out_of_stock = 'pastrami'
print(f"We have run out of {out_of_stock} and are cancelling those sandwich orders")

while out_of_stock in sandwich_orders:
    sandwich_orders.remove(out_of_stock)

print(f"Pending sandwich orders are: {sandwich_orders}")


#7-10
print("\n7-10")

polling_active = True
responses = {}

print("Welcome, let's start the polling")

while polling_active:
    name = input("What is your name? ")
    response = input(f"What is the one dream place you wan to travel to [polling active = {polling_active}]? ")
    responses[name] = response;

    poll_again = input("Would you like to continue (yes/no)? ")
    if poll_again == 'no':
        polling_active = False

print(f"Polling results are:")
for name, country in responses.items():
    print(f"{name} would love to visit {country}!")
