import random
names_string = input('give me everybodys name, seperated by a comma. ')
name = names_string.split(', ')
x=len(name)
y=random.randint(0, x)
print(name[y])