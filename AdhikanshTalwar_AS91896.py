import random 
from thewords import words

ascii = """
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""
print(ascii)
chosen_word = random.choice(words)

place_holder = ""
chosen_dashes = len(chosen_word)
correct_letter = []
game_over = False
lives = 6

for postion in chosen_word:
    place_holder += "_"

print(place_holder)

while game_over == False:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        correct_letter.append(guess)
    else:
        lives -= 1
        print(f"Wrong guess. Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("Game Over. You lose!")
            print(f"The word was: {chosen_word}")
            break

    display = ""
    for letter in chosen_word:
        if letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You Win")


