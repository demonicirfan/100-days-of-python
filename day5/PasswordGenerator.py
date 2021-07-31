import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")
)
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level
initial_password = []
for letter in range (0, nr_letters):
    l=random.randint(0,48)
    random_letters_array=letters[l]
    initial_password. append(random_letters_array)
    
for number in range (0, nr_numbers):
    l=random.randint(0,8)
    random_numbers_array=numbers[l]
    initial_password. append(random_numbers_array)

for symbol in range (0, nr_symbols):
    l=random.randint(0,8)
    random_symbols_array=symbols[l]
    initial_password. append(random_symbols_array)
    
pass_len=len(initial_password)

# hard level
final_password=[]
for i in range(1, pass_len):
    num =  random.randint(1, pass_len-1)
    x = initial_password[num]
    final_password.append(x)
for i in range(1, pass_len-1):
    print(final_password[i], end="")
