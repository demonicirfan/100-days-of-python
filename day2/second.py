# num = input("enter the number ")
# converted_string = str(num)
# first_digit = converted_string[0]
# second_digit = converted_string[1]
# result = int(first_digit)+int(second_digit)
# print(result)

#!----priority order------
#!  ()
#!  **
#!  * /
#!  + -

# * BMI Calculator

# height = input("enter your height in m: ")
# weight = input("enter your wight in kg: ")
# x = int(height)
# y = int(weight)
# BMI = y/(x*x)
# print(float(BMI))

# print(8 // 3)  # flow division

# score = 0
# height = 1.8
# iswinning = True

# #? flow string
# print(f"your score is {score}, your height is {height}, your are winning is {iswinning}")

# ## age calculator
# age = input('what is your current age? ')
# x = int(age)
# y = int(90 - x)
# print("number of days left: ", y*365)
# print("number of weaks left: ", y*52)
# print("number of hours left: ", y*8760)

# ##tip calculator
print("welcome to tip calculator")
total_bill= int(input("what was the total bill? "))
x = input("what percentage tip would you like to give 10, 12, or 15 ") 
y=int(x)
z=y/100
a=total_bill*z
b=total_bill-a
tip=total_bill-b
print(f"final tip = {tip}")

##important --> "{:.2f}"