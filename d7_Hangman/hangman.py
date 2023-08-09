import random

from d7_Hangman.art_hangman import stages
from d7_Hangman.art_hangman import hangman_start
from d7_Hangman.word_list import word_list

display = []
chosen_word = random.choice(word_list)
end = False
lives = 6
print(chosen_word)

for i in chosen_word:
    display.append('_')
print(hangman_start)
print(display)

while not end:
    guess = input('Guess one letter: ').lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
        print(display)
        if '_' not in display:
            end = True
            print('You won!')
    else:
        lives -= 1
        if lives == -1:
            end = True
            print(stages[6])
            print(f'Game Over!, {chosen_word} was the the correct word')
        else:
            print(f'{lives} remaining')
            print(stages[-lives - 2])
