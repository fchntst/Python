from random import seed  # seed = σπορος
from random import randrange
from datetime import datetime # all 3 at the beginning

kind = {"heart", "diamond", "shape", "club"}
number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}

deck = {(k, n) for k in kind for n in number}

player1 = set()
player2 = set()

list_deck = list(deck)
for i in range(5):
    position1 = randrange(len(list_deck))
    player1.add(list_deck.pop(position1))
    position2 = randrange(len(list_deck))
    player2.add(list_deck.pop(position2))

print("player1: " + str(player1))
print("player2: " + str(player2))

cnt = 0
for card in player1:
    if card[1] == "ace":
        cnt += 1
if cnt == 4:
    print("player1 has four of a kind")
cnt = 0
for card in player2:
    if card[1] == "ace":
        cnt += 1
if cnt == 4:
    print("player2 has four of a kind")
    
hand_numbers = []
for card in player1:
    if card[1] == "ace":
        hand_numbers.append(1)
    elif card[1] == "jack":
        hand_numbers.append(11)
    elif card[1] == "queen":
        hand_numbers.append(12)
    elif card[1] == "king":
        hand_numbers.append(13)
    else:
        hand_numbers.append(card[1])

hand_numbers.sort()
for pos in range(4):
    if hand_numbers[pos] != hand_numbers[pos + 1] -1:
        break
else:
    print("player2 has a straight flush")

hand_numbers = []
for card in player2:
    if card[1] == "ace":
        hand_numbers.append(1)
    elif card[1] == "jack":
        hand_numbers.append(11)
    elif card[1] == "queen":
        hand_numbers.append(12)
    elif card[1] == "king":
        hand_numbers.append(13)
    else:
        hand_numbers.append(card[1])

hand_numbers.sort()

for pos in range(4):
    if hand_numbers[pos] != hand_numbers[pos + 1] -1:
        break
else:
    print("player1 has a straight flush")
