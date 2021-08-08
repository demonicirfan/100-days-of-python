def prime_number_checker(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
    else:
        print(num, "is a prime number")


num = int(input("enter a number "))
prime_number_checker(num)
