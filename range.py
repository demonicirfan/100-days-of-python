# for number in range(1, 10, 3):
#     print(number)

# total = 0 
# for number in range (1, 101):
#     total += number
# print(total)

#! sum of all the even numbers from 1 to 100 
total =0 
for number in range(0,101,2):
    total += number
print(total)
#? or
total =0
for number in range (1,101):
    if number%2==0:
        total+= number
    else:
        total+=0
print(total)