#9-13

from die import Die

def roll_die(die: Die) -> None:
    for i in range(10):
        print(f"Rolling die {i}: {die.roll_die()}")

print("Created first die")
roll_die(Die())
print("Created second die")
roll_die(Die(10))
