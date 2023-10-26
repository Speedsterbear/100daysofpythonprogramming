import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
comp_cards = []


def deal_card():
    card = random.choice(cards)
    return card


def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def comp():
    while cal_score(comp_cards) < 17:
        comp_cards.append(deal_card())
    while cal_score(comp_cards) == 11 and 11 in comp_cards and sum(comp_cards) > 21:
        comp_cards.remove(11)
        comp_cards.append(1)
    while cal_score(comp_cards) == 0:
        break
    if cal_score(user_cards) > 21:
        print("User busts. Computer wins.")
    elif cal_score(comp_cards) > 21:
        print("Computer busts. User wins.")
    elif cal_score(user_cards) == cal_score(comp_cards):
        print("It's a draw.")
    elif cal_score(comp_cards) == 0:
        print("Computer has a Blackjack. Computer wins.")
    elif cal_score(user_cards) == 0:
        print("User has a Blackjack. User wins.")
    elif cal_score(comp_cards) > cal_score(user_cards):
        print("Computer Wins")
    else:
        print("User Wins")


user_cards.append(deal_card())
user_cards.append(deal_card())
comp_cards.append(deal_card())
comp_cards.append(deal_card())
print(user_cards)
print(comp_cards)

if cal_score(user_cards) == 0 or cal_score(comp_cards) == 0:
    comp()
else:
    while cal_score(user_cards) < 21 and input('Do you want another card? Type "y" for YES or "n" for NO: ') == 'y':
        user_cards.append(deal_card())
        print(f'This is your cards {user_cards}')
        if cal_score(user_cards) == 1:
            print(f"Your score is {sum(user_cards)}. You lose.")
            comp()
            break

# Add a message to indicate when the user's turn is over.
if cal_score(user_cards) < 21:
    print("User stands. It's the computer's turn.")
    comp()
