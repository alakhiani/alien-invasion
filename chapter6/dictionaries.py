#6-1
print('\n#6-1')
person = {
    'first_name' : 'John',
    'last_name' : 'Travolta',
    'age' : 69,
    'city' : 'Englewood',
}

print(f"First name: {person['first_name']}")
print(f"Last name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")


#6-2
print('\n#6-2')

fav_nums = {
    'Jaden' : 1,
    'Mamta' : 3,
    'Avinash' : 5,
    'Pankaj' : 7,
    'Sahil' : 9,
}

for key in fav_nums.keys():
    print(f"Key: {key}, Value: {fav_nums[key]}")

#6-3
print('\n#6-3')

words_dict = {
    'bus' : 'a large vehicle that carries people',
    'ball' : 'a spherical object to play with',
    'piston' : 'part of the engine of a car',
    'fan' : 'an object that has blades and spins to suck or blow air',
    'bike' : 'a two-wheeler that can be manual or motorized',
}

for word, meaning in words_dict.items():
    print(f"{word} : {meaning}")

#6-4
print('\n#6-4')
print("Same as above #6-3")


#6-5
print('#6-5')
rivers_dict = {
    'nile' : 'egypt',
    'amazon' : 'brazil',
    'yangtze' : 'china',
    'iguazu' : 'brazil'
}

for river, country in rivers_dict.items():
    print(f"The {river} flows through the country of {country}")

print(f"Our dictionary has the following rivers: ", end=' ')
for river in rivers_dict.keys():
    print(f"{river}", end=', ')
print()

print(f"Our dictionary has the following countries: {set(rivers_dict.values())}")


#6-6
print('\n#6-6')

people_to_poll = ['Mamta', 'Jaden', 'Pankaj', 'Sahil', 'Priyanka']

poll_dict = {
    'Mamta' : 'python',
    'Jaden' : 'scratch',
    'Pankaj' : 'c#',
}

for person in people_to_poll:
    if person not in poll_dict.keys():
        print(f"{person}, we invite you to take the favorite languages poll please!")
    else:
        print(f"Thank you for your vote {person}!")


#6-7
print('\n#6-7')

people_list = [
    { 'first_name' : 'Jack', 'last_name' : 'Ryan', 'city' : 'McLean' },
    { 'first_name' : 'Moby', 'last_name' : 'Dick', 'city' : 'Pittsfield' },
    { 'first_name' : 'Forrest', 'last_name' : 'Gump', 'city' : 'Greenbow' },
]

for person in people_list:
    print(f"First name: {person['first_name']}, Last name: {person['last_name']}, City: {person['city']}")

#6-10
print('\n#6-10')

fav_nums_dict = {
    'Jaden' : [1, 5],
    'Mamta' : {3},
    'Avinash' : {5, 7},
    'Pankaj' : {'five': 5, 'nine' : 9, 'nine' : 0},
    'Sahil' : [9, 11, 13, 13],
}

for name, fav_nums in fav_nums_dict.items():
    print(f"Name: {name}, Favorite numbers: {set(fav_nums)}")


#6-12
print('\n#6-12')

name = 'Mamta'
fav_nums_dict[name] = {9, 12}
print(f"{name} favorites: {fav_nums_dict[name]}")

name = 'Pankaj'
fav_nums_dict[name]['nine'] = 9
print(f"{name} favorites: {fav_nums_dict[name]}")
