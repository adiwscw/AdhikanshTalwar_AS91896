#Set up the random module and import the set of words

import random
from termcolor import colored
from thewords import words



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





    print(colored("========================================================", 'red'))
    print(colored("========================================================", 'red'))
    print(colored("========================================================", 'red'))
    print(colored(ascii, 'yellow'))
#Choose a random word from the list
    chosen_word = random.choice(words)
    guessed_letters = []

    place_holder = ""
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

    print(colored(place_holder, attrs=['bold']))

#Continue running the game until the game isnt over
    while game_over == False:
        guess = input("Guess a letter: ").lower()
        print(colored("------------------------", 'red'))

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter exactly one letter.")
            print(colored("------------------------", 'red'))
            continue  


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
            print("👨You Win👨")

        if guess not in chosen_word:
            lives -= 1 
        if lives == 0:
            print("💀You lose💀")
            print(colored("------------------------", 'cyan'))
            print(f"The correct word was {chosen_word}")
            print(colored("------------------------", 'cyan'))
            game_over = True

#Print the hangman ascii art and make it show the correct stages
        print(colored(stages[lives], 'green'))

        print(colored(display, attrs=['bold']))
        print(colored("------------------------", 'red'))
        guessed_letters.append(guess)
        print(f"Guessed Letters: {guessed_letters}")
        print(colored("------------------------", 'red'))
            



def instructions():
    print("\n--- Instructions ---")
    print("Welcome to Hangman!")
    print("1. Try to guess the hidden word one letter at a time.")
    print("2. Each incorrect guess adds to the hangman drawing.")
    print("3. The game ends when you guess the word or the man is fully hanged.")
    print("4. Good luck!\n")



while True:
    play_game()
    again = input(colored("Play again? y/n: ", 'white', 'on_dark_grey')).lower()
    if again != "y":
        print("👋Thanks for playing👋")
        break


while True:
    print("Welcome to Hangman!")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        play_game()
    elif choice == "2":
        instructions()
    elif choice == "3":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please choose 1, 2, or 3.\n")


