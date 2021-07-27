# print("welcome to the rollercoster!")
# height = input("what is your height in cm : ")

# if height > 120:
#         print("you can ride the rollercoaster!")
# else:
#         print("you can not ride the roller coaster")

# }                      IF ELSE
# number = int(input("which number do you want to check : "))
# if number % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

# {                    NESTED IF ELSE
# height = int(input("what is your height in cm : "))
# age = int(input("what is your age : "))
# if height > 120:
#     if age > 18:
#         print("you can have the roller coaster ride")
#     else:
#         print("sorry you can not have a roller coaster ride")
# else:
#     print("number is odd")
# }                     BMI CALCULATOR
# height = float(input("enter your height in m : "))
# weight = float(input("enter your weight in kg : "))

# bmi = round(weight/height**2)
# x = bmi
# if x < 18.5:
#     print("underweight")
# else:
#     if x < 25:
#         print("normal weight")
#     else:
#         if x < 30:
#             print("overwight")
#         else:
#             if x < 35:
#                 print("obese")
#             else:
#                 print("clinically obese")
# {                       LEAP YEAR
# year = int(input("enter the year to check : "))
# if year % 4 == 0:
#     if year % 100 != 0:
#         print("this is a leap year")
#     elif year % 400 == 0:
#         print("this is a leap year")
#     else:
#         print("not a leap year")

# else:
#     print("not a leap year")

# flow charts makes understanding easy

# {  ADDING PHOTOS TO THE ROLLER COASTER RIDES
# height = int(input("what is your height : "))
# age = int(input("what is your age : "))
# photo = input("do you want a photo say yes or no ")
# if height > 120:
#     if age > 12:
#         if photo == "yes":
#             print(f"your total bill is ${5+3}")
#         else:
#             print("you have to pay $5 ")
#     elif age < 18:
#         if photo == "yes":
#             print(f"your total bill is ${7+3}")
#         else:
#             print("you have to pay $7 ")
#     else:
#         if photo == "yes":
#             print(f"your total bill is ${12+3}")
#         else:
#             print("you have to pay $12 ")
# else:
#     print("you can not ride")
# }   PIZZA ORDER PROGRAM
# print("welcome to pyhton deleveries 🍕")
# size = input("what size pizza do you want - small, medium or large : ")
# add_pepperoni = input("do you want pepperoni? ")
# extra_cheese = input("do you want extra cheeze? ")

# if size == "small":
#     bill = 15
# elif size == "medium":
#     bill = 20
# elif size == "large":
#     bill = 25

# if add_pepperoni == "yes":
#     if size == "small":
#         bill += 2
#     else:
#         bill += 3
#     if extra_cheese == "yes":
#         bill += 1
#     else:
#         print(f"your bill is ${bill}")
# else:
#     if extra_cheese == "yes":
#         bill += 1
#     else:
#         print(f"your bill is ${bill}")


# logic operatores

# }            MIDD LIFE CRISIS
# height = int(input("what is your height : "))
# age = int(input("what is your age : "))
# if height > 120:
#    print("you can ride the roller coaster!")
#    age = int(input("what is your age"))
#    if age < 12:
#        bill = 5
#        print("child tckets are $5.")
#    elif age <=18:
#        bill = 5
#        print("child tckets are $5.")
#    elif age >= 40 and age <= 55:
#        print("everything is okey have a rollercoaster ride for free!")
#    else:
#        bill = 12
#        print("adult tickets are $12")

#    want_photo = input("do you want a photo taken? y or n. ")
#    if want_photo == "y":
#        bill +=3
#        print(f"your tatal bill = ${bill}")
#    else:
#        print(f"your total bill = ${bill}")

print("welcome to love calculator")
name1 = input("what is your name? ")
name2 = input("what is their name? ")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
love_score_int= int(love_score)
if love_score_int<10 or love_score_int>90:
    print(f"your love score is {love_score_int}, you go together like coke and mintos")
elif love_score_int>=40 or love_score_int<=50:
    print(f"your love score is {love_score_int}, you are alright together")
else:
    print(f"your score is {love_score_int}")