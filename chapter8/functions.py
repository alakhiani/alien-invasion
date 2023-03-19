import cars
from sandwich import make_sandwich as ms
from messages import send_messages
from album import *

#8-1
print("\n#8-1")

def display_message():
    """This function displays what I am learning in this chapter"""
    print("I am learning about Python functions")

display_message()

#8-2
print("\n#8-2")

def favorite_book(book):
    """This function prints what my favorite book is, based on the input argument
    book: The title of the book"""
    print(f"One of my favorite books is {book.title()}")

favorite_book("Python Crash Course")

#8-3
print("\n#8-3")

def make_shirt(size, message):
    """This function makes a shirt of the provided size, with the provided message printed on the front"""
    print(f'I have made a shirt of size {size} with the message printed on the front as "{message}"')

make_shirt('M', "This is a medium shirt")
make_shirt(message='This is a large shirt', size='L')

#8-4
print("\n#8-4")

def make_shirt_2(size='L', message='I love Python'):
    """This is a modified version of the function that makes a shirt with a provided size"""
    print(f'I have made a shirt of size {size} with the message printed on the front as "{message}"')

make_shirt_2()
make_shirt_2('M')
make_shirt_2('S', 'My shirt is too small')
make_shirt_2(message='This shirt is backwards')
make_shirt_2(size='XL')

#8-5
print("\n#8-5")

def describe_city(city, country='United States'):
    """This function tells us which country the city is in
    city: Name of the city
    country: name of the country"""
    print(f"{city} is in {country}")

describe_city("Dallas")
describe_city("Houston", "US")
describe_city("Paris", "France")
describe_city(city="London", country="UK")
describe_city(country="Germany", city="Berlin")
describe_city('Madrid', country='Spain')


#8-6
print("\n#8-6")

def city_country(city, country):
    """This function take a city and country and returns a formatted output as City, Country"""
    return f"{city}, {country}".title()

print(f"{city_country('London', 'United Kingdom')}\n")
print(f"{city_country('Paris', 'France')}\n")
print(f"{city_country('Madrid', 'Spain')}\n")

#8-7
print("\n#8-7")

album = make_album('Michael Jackson', 'Dangerous')
print(album)
album = make_album(title='Bad', artist='Michael Jackson')
print(album)
album = make_album('Pitbull', 'Armando', 10)
print(album)


#8-8
print("\n#8-8")

# Modify the loop below to while True to accept user input
while None:
    artist_in = input("Enter an artist name (type 'q' to quit at any time): ")
    if artist_in == 'q':
        break;
    
    title_in = input("Enter a title from this artist (type 'q' to quit at any time): ")
    if title_in == 'q':
        break;

    num_of_songs_str = input("Enter the number of songs in this album (use -1 if unsure, type 'q' to quit at any time): ")
    num_of_songs_in = None
    if num_of_songs_str == 'q':
        break;
    elif num_of_songs_str.isdigit():
        num_of_songs_in = int(num_of_songs_str)
        if num_of_songs_in <=0:
            num_of_songs_in = None
    
    album = make_album(artist=artist_in, title=title_in, num_of_songs=num_of_songs_in)
    print(album)


#8-9
print("\n#8-9")

def show_messages(text_messages):
    """Prints all the messages in the text_messages list"""
    if isinstance(text_messages, list):
        for message in text_messages:
            print(message)
    else:
        raise ValueError(f"Error: expecting list argument of text_messages, instead got {text_messages}")
    
messages = [
    "My first messages",
    "The second message",
    "And a third message",
    "Fourth is too much",
    "Stop at fifth"
]

show_messages(messages)
    

#8-10
print("\n#8-10")
    
sent_text_messages = []
copy_of_messages = messages[:]
send_messages(messages, sent_text_messages)
print(f"Messages list: {messages}")
print(f"Sent messages list: {sent_text_messages}")

#8-11
print("\n#8-11")

sent_text_messages.clear()
send_messages(copy_of_messages[:], sent_text_messages)
print(f"Messages list: {copy_of_messages}")
print(f"Sent messages list: {sent_text_messages}")

#8-12
print("\n#8-12")

ms("ham", "cheese")
ms()
ms("butter")
ms("tomato", "onion", "cucumber", "salami")


#8-13
print("\n#8-13")

def build_profile(first_name, last_name, **user_info):
    """Builds the user profile for the provided first and last name, along with a variable dictionary of attributes"""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name

    return user_info

user = build_profile('Jack', 'Star', age=34, phone='555-555-5555', email='jack.star@email.com')
print(user)
user = build_profile(last_name='Sparrow', first_name='Black', sex='Male', occupation='Pilot', status='Retired')
print(user)


#8-14
print("\n#8-14")

car = cars.make_car('Ferrari', 'Spider')
print(car)
car = cars.make_car('Mazda', '6', package='Grand Touring', color = 'Blue', gps=True)
print(car)
