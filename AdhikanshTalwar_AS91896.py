#Import all the required modules
import random
from termcolor import colored
from thewords import words

def play_game():
    # Game title ASCII art
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


    # Choose a random word from the list
    chosen_word = random.choice(words)
    guessed_letters = []
    correct_letter = []
    lives = 6
    game_over = False
    placeholder = ""

    # Hangman drawing stages for each wrong guess
    easy_stages = [
        """
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
  =====""",
  """
   +--+
      |
      |
      |
      |
      |
  =====
   """,
   """
      
      |
      |
      |
      |
      |
  =====
   """,
   """  
      |
      |
      |
      |
  =====
   """,
   """  
      
      |
      |
      |
  =====
   """,
   """  
      
      
      |
      |
  =====
   """
    ]

    hard_stages = [
        """
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
  ====="""
    ]

    # Build initial blank display
    for letter in chosen_word:
        placeholder += "_"
    print(colored(placeholder, attrs=['bold']))

    # Main game loop
    while not game_over:
        guess = input("Guess a letter: ").lower()
        print(colored("------------------------", 'red'))

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter exactly one letter.❌")
            print(colored("------------------------", 'red'))
            continue

        display = ""

        # Build display based on guessed letters
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letter.append(guess)
            elif letter in correct_letter:
                display += letter
            else:
                display += "_"

        # Win check
        if "_" not in display:
            game_over = True
            print("👨 You Win 👨")

        # Wrong guess handling
        if guess not in chosen_word:
            lives -= 1
        if lives == 0:
            print(colored("💀 You lose 💀", 'cyan'))
            print(colored("------------------------", 'red'))
            print(colored(f"The correct word was {chosen_word}", 'cyan'))
            print(colored("------------------------", 'red'))
            game_over = True

        # Show current hangman and game state
        print(colored(hard_stages[lives], 'green'))
        print(colored(display, attrs=['bold']))
        print(colored("------------------------", 'red'))

        guessed_letters.append(guess)
        print(colored(f"Guessed Letters: {guessed_letters}", 'yellow'))
        print(colored("------------------------", 'red'))

def instructions():
    print(colored("\n--- Instructions ---", 'cyan'))
    print("Welcome to Hangman!")
    print("1. Try to guess the hidden word one letter at a time.")
    print("2. Each incorrect guess adds to the hangman drawing.")
    print("3. The game ends when you guess the word or the man is fully hanged.")
    print("4. Good luck!\n")

# Main menu loop
while True:
    print("Welcome to Hangman!")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        while True:
            play_game()
            again = input("Play again? (y/n): ").strip().lower()
            if again != "y":
                print("👋Thanks for playing👋")
                exit()
    elif choice == "2":
        instructions()
    elif choice == "3":
        print("👋Hope you play it later!👋")
        exit()
    else:
        print("❌Invalid input. Please choose 1, 2, or 3.❌\n")
