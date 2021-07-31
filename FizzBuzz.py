end_num = int(input('how many number you want to check '))
for number in range (2, end_num):
    if number % 3==0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
