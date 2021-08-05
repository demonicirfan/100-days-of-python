# step 1
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

choosen_word = random.choice(word_list)
choosen_word_length = len(choosen_word)

print('guessed word is ' + choosen_word)

display = []

for _ in range(choosen_word_length):
    display += "_"
        
i=1
score = 0
for i in range(choosen_word_length):
    guess = input('Guess a letter: ').lower()

    for position in range(choosen_word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
        else:
            score = score + 1
    if score == choosen_word_length:
        print(stages[i])
        i=i+1
        
    score = 0
 #   life = choosen_word_length - i
 #  print(f'punishment you have {life} life left')
    print(display)
    


l = list(choosen_word)
if display == l:
    print("\nYou won")

else:
    print("\nyou lost")
