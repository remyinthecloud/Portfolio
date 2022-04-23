import os
import random
from hangman_art import *
from hangman_words import *

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

guesses = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('clear')
    
    for similar in guess:
      guesses.append(guess)
      similar_guesses = guesses.count(similar)
      if similar_guesses > 1:
        print(f"You already guesses {guess}.")
      
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word and similar_guesses > 1:
        print("I'll spare a life for you this time. Don't do it again!")
    elif guess not in chosen_word:
        print(f"The letter {guess} is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])