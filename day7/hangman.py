import random

import hangman_art
import hangman_words

print(hangman_art.logo)

choosen_word = random.choice(hangman_words.word_list)
choosen_word_length = len(choosen_word)

print('guessed word is ' + choosen_word)

display = []
lives = 6

for _ in range(choosen_word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
          print(f"You have already guessed {guess}")
    for position in range(choosen_word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in choosen_word:
        print(f"You gussed {guess}, that's not in the word. You loose a life ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(hangman_art.stages[lives])
    
