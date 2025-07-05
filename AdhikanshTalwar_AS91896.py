# Import all the required modules
import random
from termcolor import colored
from thewords import words

# Global variable for difficulty and setting the main game function
difficulty = "hard"

def play_game():
    global difficulty

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
    print(chosen_word)
    guessed_letters = []
    correct_letter = []

    # ASCII art stages for different life counts
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
  =====""",
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
   """,
   """  
      
      
      
      |
  =====
   """,
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

    # Set lives and stages based on difficulty
    if difficulty == "easy":
        lives = 12
        stages = easy_stages
    else:
        lives = 6
        stages = hard_stages

    game_over = False
    placeholder = ""

    # Build initial blank display
    for letter in chosen_word:
        placeholder += "_"
    print(colored(placeholder, attrs=['bold']))

    # Main game loop
    while not game_over:
        guess = input(colored("Guess a letter: ", attrs=['bold'])).lower()
        print(colored("------------------------", 'red'))

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print(colored("Invalid input. Please enter exactly one letter.", 'red'))
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
            print(colored("You Win", 'green', attrs=['bold']))

        # Wrong guess handling
        if guess not in chosen_word:
            lives -= 1
        if lives == 0:
            print(colored("You lose", 'red', attrs=['bold']))
            print(colored("------------------------", 'red'))
            print(colored(f"The correct word was {chosen_word}", 'red', attrs=['bold']))
            print(colored("------------------------", 'red'))
            game_over = True

        # Show current hangman and game state
        print(colored(stages[lives]))
        print(colored(display, attrs=['bold']))
        print(colored("------------------------", 'red'))

        guessed_letters.append(guess)
        print(colored(f"Guessed Letters: {guessed_letters}", 'yellow', attrs=['bold']))
        print(colored("------------------------", 'red'))

def instructions():
    print(colored("\n--- Instructions ---", 'cyan'))
    print("Welcome to Hangman.")
    print("1. Try to guess the hidden word one letter at a time.")
    print("2. Each incorrect guess adds to the hangman drawing.")
    print("3. The game ends when you guess the word or the man is fully hanged.")
    print("4. In Easy mode, you get more lives (11). In Hard mode, you get fewer lives (6).\n")

# Main menu loop
while True:
    print("Welcome to Hangman!")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        print("\nChoose difficulty:")
        print(colored("1. Easy: 13 Lives", 'green', attrs=['bold']))
        print(colored("2. Hard: 6 Lives", 'red', attrs=['bold']))
        diff_choice = input("Enter your choice (1/2): ").strip()

        # Setting the difficulties
        if diff_choice == "1":
            difficulty = "easy"
        elif diff_choice == "2":
            difficulty = "hard"
        else:
            print("Invalid difficulty. Defaulting to easy.", 'red')
            difficulty = "easy"

        while True:
            play_game()
            again = input("Play again? (y/n): ").strip().lower()
            if again != "y":
                print(colored("Thanks for playing", 'green'))
                exit()
    elif choice == "2":
        instructions()
    elif choice == "3":
        print(colored("Hope you play it later!", 'green'))
        exit()
    else:
        print(colored("Invalid input. Please choose 1, 2, or 3.\n", 'red'))
