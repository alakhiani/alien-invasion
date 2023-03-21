from pathlib import Path
import json

print("\n#10-1 Learning Python")

path = Path('learning_python.txt')
file_content = path.read_text()
print(file_content)

lines = file_content.splitlines()
line_num = 0
for line in lines:
    line_num += 1
    print(f"Line {line_num}: {line}")
    
print(f"Total lines: {line_num}, File length: {len(file_content)}, Lines in split: {len(lines)}")


print("\n#10-2 Learning C")

for line in lines:
    print(f"{line.replace('Python', 'C')}")


print("\n#10-3 Simpler Code")

for line in file_content.splitlines():
    print(f"{line.replace('Python', 'Java')}")


print("\n#10-4 Guest")

guest = input(f"Please enter your name: ")

path = Path('guest.txt')
path.write_text(guest)



print("\n#10-5 Guest Book")

file_content = ''
while True:
    user_input = input(f"Please enter the names one by one (type 'q' to quit): ")
    if user_input == 'q':
        break
    else:
        file_content += user_input + '\n'

path = Path('guest_book.txt')
path.write_text(file_content)


print("\n#10-6 Addition")

while True:
    str_1 = input("Enter the first number to add (type 'q' to quit): ")
    if str_1 == 'q':
        break

    str_2 = input("Enter the second number to add (type 'q' to quit): ")
    if str_2 == 'q':
        break

    try:
        result = int(str_1) + int(str_2)
    except ValueError:
        print(f"Please enter integers for the addition, values you provided were [{str_1}, {str_2}]")
    else:
        print(f"{str_1} + {str_2} = {result}")

print('Thank you for using the addition calculator')


print("\n#10-8 Cats and Dogs")

files = ['sheep.txt', 'cats.txt', 'horses.txt', 'dogs.txt', 'hamsters.txt']

for file in files:
    path = Path(file)
    try:
        file_content = path.read_text()
    except FileNotFoundError:
        print(f"Could not fine file {file}")
    else:
        print(file_content)


print("\n#10-10 Common Words")

file_name = 'pg70327.txt'
path = Path(file_name)

try:
    file_content = path.read_text()
except FileNotFoundError:
    print(f"Could not find file {file_name}")
else:
    search_word = 'book'
    search_word_appearances = file_content.lower().count(search_word)
    print(f"The word {search_word} appears {search_word_appearances} times in the file {file_name}")


print("\n10-11 Favorite Number")

fav_num = input(f"What is your favorite number? ")
path = Path('favorite_number.txt')
path.write_text(json.dumps(fav_num))

file_content = path.read_text()
read_fav_num = json.loads(file_content)
print(f"I know your favorite number, it is {read_fav_num}")


print("\n10-13 User Dictonary")

file_name = 'fav_num.txt'
path = Path(file_name)
if path.exists():
    file_content = path.read_text()
    read_fav_num = json.loads(file_content)
    print(f"Your favorite number is {read_fav_num}")
else:
    fav_num = input(f"What is your favorite number? ")
    file_content = json.dumps(fav_num)
    path.write_text(file_content)


print("\n#10-13 User Dictionary")

user_info = {}
user_info['first_name'] = input("Please enter your first name: ")
user_info['last_name'] = input("Please enter your last name: ")
user_info['age'] = input("Please enter your age: ")

file_name = 'remember_me.txt'
path = Path(file_name)
path.write_text(json.dumps(user_info))

file_content = path.read_text()
user_info = json.loads(file_content)
print(user_info)
