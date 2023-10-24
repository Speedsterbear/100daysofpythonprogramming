import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
comp_cards = []


def deal_card():
    card = random.choice(cards)
    return card


user_cards.append(deal_card())
user_cards.append(deal_card())
comp_cards.append(deal_card())
comp_cards.append(deal_card())
print(user_cards)
print(comp_cards)


def cal_score(cards_sec):
    if sum(cards_sec) == 21:
        return 0

    if 11 in cards_sec and sum(cards_sec) > 21:
        cards_sec.remove(11)
        cards_sec.append(1)
        print(cards_sec)


