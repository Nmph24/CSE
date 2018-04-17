import random  # This should be on line 1
#  # This is working
# print("hello world")
#
# # arbin saucedo
#
# print(5 + 3)
# print(5 - 5)
# print(7 * 9)
# print(7**2 * 9 )
# print(6 / 2)
# print(3 ** 2)
#
# print() # this makes a new line. In 3.6, it looks like: print()
# print("See if you can figure this out")
# print(10 % 3)
#
# car_name = "acc. more than a ak"
# car_type = "rekt-9"
# car_cylinders = 8
# car_mpg = 9000.1
#
# # InLine printing
# print("I have a car called %s. It's a %s." % (car_name, car_type))
#
# # Asking for input
# name = input("What is your name? ") # In Python 3, it is just called input()
# print("Hello %s." % name)
#
# age = input("How Old are you? ")
# print("%s wow... You're really old you should just take a sit and rest now." % age)

# Functions


# def print_hw():
#     print("Hello World")
#
#
#
# print_hw()
# print_hw()
# print_hw()
#
# def say_hi(name): # Name is parameter
#     print("Hello %s." % name)
#     print("Enjoy your day.")
#
#
# say_hi("Jimmy John")
#
#
# def print_age(name, age):
#     print("%s is %d years old." % (name, age))
#     age += 1  # age = age + 1
#     print("Next year, they will be %d" % age)
#
#
# print_age("Jimmy John", 15)
#
# def f(x):
#     return x**3 + 4 * x**2 + 7 * x - 4
#
#
# print(f(3))
# print(f(4))
# print(f(5))
#
# # If statements
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     else:
#         return "F"
#
#
# print(grade_calc(90))
#
#
# def Happy_bday(name):
#     print("Happy Birthday to %s" % name + ",")
#     print("Happy Birthday To you" + ",")
#     print("Happy Birthday To you" + ",")
#     print("Happy Birthday toooo " + name + ".")
#
# Happy_bday("Jon")
#
#
# # loops
#
# for num in range(100):
#     print(num + 1)
#
#
# a = 1
# while a <= 10:
#     print(a)
#     a += 1
#
#
# # Random Numbers
#
#
# print(random.randint(0, 100))
#
#
# print(1 == 1) # Is 1 equal to 1??
# print(1 != 2) # Is 1 not equal to 2??
# print(10 <= 15)
# print(not False)

# Recasting

# c = '1'
# print(c == 1)
# print(int(c) == 1) # Both are ints
# print(c == str(1)) # Both are strings
#
# # The input command ALWAYS gives a string
#
# # Lists
# the_count = [1, 2, 3, 4, 5]
# shopping_list = ["Noodles", "Egg rolls", "Milk", "Rice", "Soda"]
#
# print(shopping_list[2])
#
# print(len(shopping_list))
#
# # Going through a list
# for item in shopping_list:
#     print(item)
#
# for number in the_count:
#     print(number * 2)
#
# len(shopping_list)  # Gives me the length of the list
# range(3)    # Gives a list of the numbers 0 through 2
# range(len(shopping_list))   # A list of EVERY index in a list
#
# for num in range(len(shopping_list)):
#     item = shopping_list[num]
#     print("The item at index %d is %s" % (num, item))
#
# # Turn things into a list
# str1 = "Hello Class!"
# listOne = list(str1)
# print(listOne)
# listOne[11] = '.'
# print(listOne)
# print("".join(listOne))
#
# # Add things to a list
# shopping_list.append("new untouched spaget")
# shopping_list.append("a cold one")
# print(shopping_list)
# shopping_list.pop(0)
# print(shopping_list)
#
# # the string class
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.punctuation)
# print(string.digits)
#
# # Dealing with strings
# strTwo = "ThIS Is A vEry oDD sENteNCe"
# lowercase = strTwo.lower()
# print(lowercase)
#
# # Dictionaries
# dictionary = {'name': 'Lance', 'age': 23, "height": 5 * 12 + 7}
#
# # Accessing Dictionaries
# print(dictionary['name'])
# print(dictionary['age'])
# print(dictionary['height'])
#
# # Adding to a dictionary
# dictionary['weight'] = 280
# print(dictionary)
#
# large_dictionary = {
#     'CA': 'California',
#     'FL': 'Florida',
#     'OH': 'Ohio'
# }
# print(large_dictionary['FL'])
#
# larger_dictionary = {
#     'CA': [
#         'Fresno',
#         'Sacramento',
#         'Los Angeles'
#     ],
#     'FL': [
#         "Tampa",
#         "Orlando",
#         "Miami"
#     ],
#     'OH': [
#         "Cleavland",
#         "Cincinnati",
#         "Columbus"
#     ]
# }
#
# print(larger_dictionary['FL'])
# print(larger_dictionary['FL'][2])
# print(larger_dictionary['OH'][1])
#
# largest_dictionary = {
#     'CA': {
#         'NAME': 'California',
#         'POPULATION': 39250000,
#         'BORDER ST': [
#             'Oregon',
#             'Nevada',
#             'Arizona'
#         ]
#     },
#     'AZ': {
#         'NAME': 'Arizona',
#         'POPULATION': 6931000,
#         'BORDER ST': [
#             'California',
#             'Utah',
#             'Nevada',
#             'New Mexico'
#         ]
#     },
#     'NY': {
#         'NAME': "New York",
#         'POPULATION': 19750000,
#         'BORDER ST': [
#             'Vermont',
#             'Massachusetts',
#             'Connecticut',
#             'Pennsylvania',
#             'New Jersey'
#         ]
#     }
# }
#
# current_node = largest_dictionary['CA']
# print(current_node)
# print(current_node['NAME'])
# print(current_node['POPULATION'])

# Defining Functions
def hello_world():
    print("Hello World")


hello_world()


def square_it(number):
    return number ** 2


print("The number is %d" % square_it(3))


def tip_calc(subtotal):
    tax_amt = subtotal * 0.18   # tax_amt CANNOT be used outside of the def!!
    return tax_amt


def total_bill(bill_amt):
    total = bill_amt + tip_calc(bill_amt)
    print("Your total bill is %d" % total)


total_bill(100)


def distance(x1, y1, x2, y2):
    inside = (x2 - x1) ** 2 + (y2 - y1) ** 2
    answer = inside ** 0.5    # This is a square root
    return answer


print(distance(0, 0, 3, 4))


def pythagorean(a, b):
    inside = (a ** 2 + b ** 2)
    answer = inside ** 0.5
    return answer


print(pythagorean(5, 12))
