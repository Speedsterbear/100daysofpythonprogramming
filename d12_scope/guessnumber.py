import random

import ascii

# Include an ASCII art logo.
print(ascii.logo[0])


# Allow the player to submit a guess for a number between 1 and 100.
def game(att):
    lives = att
    gn = random.randint(0, 100)
    eq = False
    # Track the number of turns remaining.
    while lives > 0 and eq == False:
        guess = int(input('Make a guess:'))
        if guess == gn:
            # If they got the answer correct, show the actual answer to the player.
            print('You win :)')
            eq = True
        # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
        elif guess > gn:
            lives -= 1
            print(f'Too high, Wrong guess. You have {lives} attempts left.')
        elif guess < gn:
            lives -= 1
            print(f'Too low, Wrong guess. You have {lives} attempts left.')
    # If they run out of turns, provide feedback to the player.
    if lives <= 0:
        print(f'You dont have lives you lost :( the number was {gn}')


print('Welcome to the Guessing Number Game')
print('Im thinking of a number between 1 to 10')
diff = input('Choose a difficulty. Type "easy" or "hard"')
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
if diff == 'easy':
    game(10)
elif diff == 'hard':
    game(5)




