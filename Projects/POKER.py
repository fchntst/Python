from random import seed
from random import randrange
from datetime import datetime 

seed(datetime.now())

cards = set()

kind = ('heart', 'diamond', 'spade', 'club')
number = ('ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king')

for i in kind:
    for j in number:
        cards.add((i, j))

list_cards = list(cards)
first_player = set()
second_player = set()

for i in range(5):
    card = randrange(len(list_cards))
    first_player.add(list_cards.pop(card))
    card = randrange(len(list_cards))
    second_player.add(list_cards.pop(card))

print('first player: ' + str(first_player))
print('second player: ' + str(second_player))


# full of kind player 1 
cnt = 0
for i in first_player:
    if i[1] == 'ace':
        cnt += 1 
if cnt == 4:
    print('first player has full of kind')

# full of kind player 2 

cnt = 0
for i in second_player:
    if i[1] == 'ace':
        cnt += 1
if cnt == 4:
    print('second player has full of kind')

# straight flush player 1 

hand_number = []
for card in first_player:
    if card[1] == 'ace':
        hand_number.append(1)
    elif card[1] == 'jack':
        hand_number.append(11)
    elif card[1] == 'queen':
        hand_number.append(12)
    elif card[1] == 'king':
        hand_number.append(13)
    else:
        hand_number.append(card[1])
hand_number.sort()

for pos in range(4):
    if hand_number[pos] != hand_number[pos + 1] - 1:
        break
else:
    print('first player has a straight flush')

hand_number2 = []
for card in second_player:
    if card[1] == 'ace':
        hand_number2.append(1)
    elif card[1] == 'jack':
        hand_number2.append(11)
    elif card[1] == 'queen':
        hand_number2.append(12)
    elif card[1] == 'king':
        hand_number2.append(13)
    else:
        hand_number2.append(card[1])
hand_number2.sort()

for pos in range(4):
    if hand_number2[pos] != hand_number2[pos + 1] - 1:
        break
else:
    print('second player has a straight flush')