import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
choice = int(input('What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS\n'))
com = [rock, paper, scissors]
com_choice = random.choice(com)

if choice == 0:
    print(rock)
    print(f'Computer chose: {com_choice}')
    if com_choice == rock:
        print('You tie')
    if com_choice == paper:
        print('You lose')
    if com_choice == scissors:
        print('You win!')
if choice == 1:
    print(paper)
    print(f'Computer chose: {com_choice}')
    if com_choice == rock:
        print('You win!')
    if com_choice == paper:
        print('You tie')
    if com_choice == scissors:
        print('You lose')
if choice == 2:
    print(scissors)
    print(f'Computer chose: {com_choice}')
    if com_choice == rock:
        print('You lose')
    if com_choice == paper:
        print('You win!')
    if com_choice == scissors:
        print('You tie')
