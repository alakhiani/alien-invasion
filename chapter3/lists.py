bikes = ['trek', 'cannondale', 'redline', 'specialized']
print(bikes)

print(f"First bike: {bikes[0].title()}")
print(f"Second last bike: {bikes[-2]}")
print(f"List lenght: {bikes.__len__()}")


# Guest List

#3.4
guest_list = ['Mamta', 'Jaden', 'Pankaj']
print(f"We will all be having dinner together on Saturday, I found a table for 4: {guest_list}");
print(f"Will you join us for dinner on Saturday {guest_list[0].title()}?")
print(f"Will you join us for dinner on Saturday {guest_list[1].title()}?")
print(f"Will you join us for dinner on Saturday {guest_list[2].title()}?")

#3.5
print(f"Folks unfortunately {guest_list[1]} will not be able to join us on Saturday!");
guest_list[1] = 'Sahil'
print(f"Will you join us for dinner on Saturday {guest_list[0].title()}?")
print(f"Will you join us for dinner on Saturday {guest_list[1].title()}?")
print(f"Will you join us for dinner on Saturday {guest_list[2].title()}?")

#3.6
print(f"Folks great news, we found a bigger table for 7 for this Saturday, we have 3 more guests joining!");
guest_list.insert(0, 'Priyanka')
guest_list.insert(2, 'Anya')
guest_list.append('Laksh');
print(f"Will you join us for dinner on Saturday {guest_list[0].title()}?")
print(f"Will you join us for dinner on Saturday {guest_list[1].title()}?")
print(f"Will you join us for dinner on Saturday {guest_list[2].title()}?")
print(f"Will you join us for dinner on Saturday {guest_list[3].title()}?")
print(f"Will you join us for dinner on Saturday {guest_list[4].title()}?")
print(f"Will you join us for dinner on Saturday {guest_list[5].title()}?")

#3.7
print(f"Sorry folks, the new table won't be available after all, I can only accomodate 2 folks to join me for dinner!")
guest_being_uninvited = guest_list.pop()
print(f"So sorry {guest_being_uninvited}, we will plan dinner another time instead")
guest_being_uninvited = guest_list.pop()
print(f"So sorry {guest_being_uninvited}, we will plan dinner another time instead")
guest_being_uninvited = guest_list.pop()
print(f"So sorry {guest_being_uninvited}, we will plan dinner another time instead")
guest_being_uninvited = guest_list.pop()
print(f"So sorry {guest_being_uninvited}, we will plan dinner another time instead")

print(f"Guests who are still invited: {guest_list}")

del guest_list[1]
del guest_list[0]

print(f"Guests left on the invite list: {guest_list}")
del guest_list


# 3.8 - Seeing the world
travel_list = ['New Zealand', 'Iceland', 'Greenland', 'Faroe Island', 'Japan']
print(f"Original List: {travel_list}")
print(f"Sorted List: {sorted(travel_list)}")
print(f"Original List: {travel_list}")
print(f"Rverse sorted List: {sorted(travel_list, reverse=True)}")
print(f"Original List: {travel_list}")
travel_list.sort()
print(f"Permanently sorted List: {travel_list}")
travel_list.sort(reverse=True)
print(f"Permanently reverse-sorted List: {travel_list}")
print(f"Print forward sorted list: {sorted(travel_list)}")
print(f"We have {len(travel_list)} countries on the list!")