# Author: Avinash Lakhiani
# Date: 2023-03-08
# Exercises in Chapter 2

message = "Hello World Python!"
print(message, end="...")

message = "Hello world again!"
print(message)

print('I told my friend "Python is my favorite language!"')
print("The language 'Python' is named after Monty Python, no the snake.")
print("One of Python's stregnths is its diverse and supportive community.")

name = "aDa loveLace"
print(name.title())
print(name.lower())
print(name.upper())

first_name="charles"
last_name="babbage"

full_name = f"{first_name} {last_name}"
print(full_name)

full_name = f'{first_name.title()} {last_name.title()}'
print(full_name)

print(f"Full name is: {full_name.upper()}")

message = f"Hello, {full_name.title()}"
print(message)

google_url = "https://www.google.com"
clean_google_url = google_url.removeprefix("https://")
print(google_url)
print(clean_google_url)

file_name_with_suffix = "filename.txt"
file_name_only = file_name_with_suffix.removesuffix(".txt")
print(file_name_only)

text = "    A string    with a    lot of spaces     "
print(text.strip())
print(f"Original string length: {text.__len__()} \
      , Stripped string length: {text.strip().__len__()} \
      , Left stripped length: {text.lstrip().__len__()} \
      , Right stripped length: {text.rstrip().__len__()}")

print(5+3)
print(2*4)
print(16/2)
print(4**2/2)
