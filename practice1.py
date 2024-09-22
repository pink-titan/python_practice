# print("Hello world")
# print('*' * 10)
# price = 10
# print(price)

# name = "Chhapa Hula"
# age = 26
# is_new = True
# print(name)
# print(age)
# print(is_new)

# name = input("What's your name? ")
# color = input("What's your favourite colour? ")
# print(name + ' likes ' + color)

# year = input("Birth year: ")
# age = 2024 - int(year)
# print(age)

# weight_pound = input("What's your weight in pound? ")
# weight_kg = float(weight_pound) * 0.454
# print(weight_kg)

# conversation = '''Hula eats rotten mangoes, bananas, apples. He enjoys these with a great mind.'''
# print(conversation)

# wish = "Want to learn python"
# print(wish[0:-3])

# first = "Hulandi"
# last = "Hula"
# msg = f"{first} [{last}] is very bad"
# print(msg)

# wish = "Want to learn python"
# print(len(wish))
# print(wish.upper())
# print(wish.lower())
# print(wish.replace('python','python properly'))
# print('learn' in wish)
# print(wish.find("e"))
# print(wish.title())

# x = 16
# x += 4
# print(x)
# x -= 3
# print(x)
# x *= 4
# print(x)
# x /= 17
# print(x)
# x **= 2
# print(x)

# x = 4.7
# print(round(x))
# print(abs(-x))
# import math
# print(math.ceil(x))
# print(math.floor(-x))


# for i in range(1,6):
#     print('*'*i)

# for i in range(1,101):
#     print(i)

# price = 1000000
# has_good_credit = True
# if has_good_credit:
#     Down_payment = price * 0.1
# else:
#     Down_payment = price * 0.2
# print(f"Down_payment: Rs {Down_payment}")

# has_high_income = True
# has_good_credit = True
# if has_high_income and has_good_credit:
#     print("Eligible for loan.")
# else:
#     print("Not eligible for loan.")

# has_high_income = False
# has_good_credit = False
# if has_high_income or has_good_credit:
#     print("Eligible for loan.")
# else:
#     print("Not eligible for loan.")

# has_high_income = True
# has_criminal_record = False
# if has_high_income and not has_criminal_record:
#     print("Eligible for loan.")
# else:
#     print("Not eligible for loan.")

# Temperature = 26
# if Temperature >= 30:
#     print("It's a hot day")
#     print("Drink plenty of water.")
# else:
#     print("It's not a hot day.")

# name = "john Smith"
# if len(name) < 3:
#     print("Name must be at least 3 characters long.")
# elif len(name) > 50:
#     print("Name must be a maximum of 50 characters long.")
# else:
#     print("Name looks good.")

# weight = float(input("What's your weight? "))
# unit = input("(L)bs or (K)g? ")
# if unit.upper() == "L":
#     converted = weight * 0.454
#     print(f"You are {converted} Kg.")
# else:
#     converted = weight / 0.454
#     print(f"You are {converted} pounds.")

# i = 1
# while i <= 100:
#     print('*' * i)
#     i = i + 2


# import random

# combination = ['rimpa', 'bula', 'hula', 'tepa', 'khepa', 'chapa']

# score = random.choice(combination)

# print(score)

# import random
# secret_number = random.randint(1, 10)
# Guess_count = 0
# Guess_limit = 3
# while Guess_count < Guess_limit:
#     Guess = int(input("Guess: "))
#     Guess_count += 1
#     if Guess == secret_number:
#         print("You won!")
#         break
# else:
#     print(f"Sorry, you failed. secret number is {secret_number}")

# comand = ""
# started = False
# while True:
#     comand = input("> ").lower()
#     if comand == "start":
#         if started:
#             print("car is already started!")
#         else: 
#             started = True
#             print("car started...")
#     elif comand == "stop":
#         if not started:
#             print("car is already stopped!")
#         else:
#             started = False
#             print("car stopped.")
#     elif comand == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit """)
#     elif comand == "quit":
#         break
#     else:
#         print("sorry, I don't understand that.")

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"total: {total}")

# for X in range(3):
#     for Y in range(3):
#         print(f"({X}, {Y})")

# numbers = [7, 2, 5, 2, 2]
# for number in numbers:
#     print("*" * number)

# numbers = [10, 10, 3, 3, 3, 7, 7, 3, 3, 3, 3]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)


import calendar

cal = calendar.calendar(2024)

print(cal)

number = [4, 6, 2, 9, 1, 7]
max = number[0]
for number in number:
    if number > max:
        max = number
print(max)

