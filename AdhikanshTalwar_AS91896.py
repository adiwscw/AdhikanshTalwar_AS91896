#Set up the random module and import the set of words

import random
from thewords import words

def ask():
    start_or_no = input("DO YOU WISH TO PLAY? y/n: ").lower()

while True:
    ask()
    start_or_no = input("DO YOU WISH TO PLAY? y/n: ").lower()
    if ask != "y":
        print("ok")
        break

#Making the game function for the play again loop

def play_game():

    ascii = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|                                                                  
                    __/ |                      
                   |___/                       
"""





    print("========================================================")
    print("========================================================")
    print("========================================================")
    print(ascii)
#Choose a random word from the list
    chosen_word = random.choice(words)

    place_holder = ""
    chosen_dashes = len(chosen_word)
    correct_letter = []
    game_over = False
    lives = 6

    stages = ["""
   +--+
   |  |
   O  |
  /|\ |
  / \ |
      |
  =====
   """,
  """
   +--+
   |  |
   O  |
  /|\ |
  /   |
      |
  =====""",
  """
   +--+
   |  |
   O  |
  /|\ |
      |
      |
  =====""",
  """
   +--+
   |  |
   O  |
  /|  |
      |
      |
  =====""",
 """
   +--+
   |  |
   O  |
   |  |
      |
      |
  =====""",
  """
   +--+
   |  |
   O  |
      |
      |
      |
  =====""",
  """
   +--+
   |  |
      |
      |
      |
      |
  ====="""]

#Print the blanks and show how many letters in the word
    for postion in chosen_word:
        place_holder += "_"

    print(place_holder)

#Continue running the game until the game isnt over
    while game_over == False:
        guess = input("Guess a letter: ").lower()

        display = ""
#Check if the user guess is correct
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letter.append(guess)
            elif letter in correct_letter:
                display += letter
            else:
                display += "_"

    
#Check for game overs
        if "_" not in display:
            game_over = True
            print("You Win")

        if guess not in chosen_word:
            lives -= 1 
        if lives == 0:
            print("You lose")
            print(f"The correct word was {chosen_word}")
            game_over = True

#Print the hangman ascii art and make it show the correct stages
        print(stages[lives])

        print(display)
        

while True:
    play_game()
    again = input("Play again? y/n: ").lower()
    if again != "y":
        print("Thanks for playing")
        break