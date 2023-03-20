from random import choice

#9-14 Lottery
print("\n#9-14")

lottery_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D')

for i in range(4):
    print(f"Any ticket matching this winning number or letter wins a prize: {choice(lottery_tuple)}")


#9-15 Lottery Analysis
print("\n#9-14")

my_ticket = (1, 5, 9, 'C')
attempts = 0

while True:
    selection = choice(lottery_tuple)
    attempts += 1
    if selection in my_ticket:
        print(f"I won for ticket {selection} on attempt {attempts}")
        break
