#4.1
my_pizzas = ['cheese pizza', 'pepperoni pizza', 'veg pizza']
for pizza in my_pizzas:
    print(f"I love {pizza}")
#4.2
print(f"I love {len(my_pizzas)} types of pizza!")


#4.3
list_to_twenty = list(range(1,21))
print(f"List to twenty: {list_to_twenty}")
#4.4
list_to_million = list(range(1,10**6+1))
print(f"Minimum and Maximum in the list_to_million is: {min(list_to_million)}, \
      {max(list_to_million)}")
#print(f"List to million {list_to_million}")
#4.5
print(f"Sum of items in range 1-1M is: {sum(list_to_million)}")
#4.6
print(f"List of odd numbers {list(range(1, 21, 2))}")
#4.7
print(f"List of mulitples of three {list(range(3, 31, 3))}")
#4.8
cubes = []
for item in range(1, 11):
    cubes.append(item**3)
print(f"Cubes of numbers from 1 to 10 is: {cubes}")
#4.9
cubes_2 = [value**3 for value in range(1, 11)]
print(f"List of cubes from 1 to 10 generated through list comprehension {cubes_2}")

#4.10
print(f"The first three items in the list are: {list_to_twenty[:3]}")
print(f"Every other item in the list is: {list_to_twenty[:20:3]}")
print(f"The last three items in the list are: {list_to_twenty[-3:-1]}")

#4.11
friends_pizzas = my_pizzas[:]
friends_pizzas.append("chicken pizza")

print(f"My pizzas: {my_pizzas}")
print(f"Friend's pizzas: {friends_pizzas}")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)

#4.13
print("Restaurant foods available are:")
foods = ('taco', 'barrito', 'bowl', 'salad', 'chips')
for food in foods:
    print(food)

# foods[1] = 'salsa'

foods = ('taco', 'barrito', 'soup', 'salad', 'salsa')
for food in foods:
    print(food)
