# step 1
import random
word_list = ["ardvark", "baboon", "camel"]

choosen_word = random.choice(word_list)
choosen_word_len = len(choosen_word)

guess = input("Guess a letter: ").lower()

#letters = list(choosen_word)

array = []

for letter in choosen_word:
    if letter == guess:
        array.append(guess)
    else:
        array.append("_")

print(array)y