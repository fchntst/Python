# making a game called memory cards game

numbers = [3, 2, 1, 4, 2, 1, 4, 3]                # 0 -> 1, 1 -> 5

cards = [
    "|" , "_" , "|", "-", "|" , "_" , "|", "-",
    "|" , "_" , "|", "-", "|" , "_" , "|", "-",
    "|" , "_" , "|", "-", "|" , "_" , "|", "-",
    "|" , "_" , "|", "-", "|" , "_" , "|", ","
]
''' there are and some other states like some card open or temp_open cards'''

for rows in cards:
    for element in rows:
        print(element, end=' ')

print('')
print('These are the cards where hidden number are inside, ')
print('Try to memorize the numbers you will find in the cards')

active_game = True
total_tries = 3

print('you have ' + str(total_tries) + ' tries')

while active_game:
    first_card = int(input('Type here a number of a position: '))
    second_card = int(input('Type here a number of a position: '))
    total_tries -= 1
    while (0 < first_card > 7) or (0 < second_card > 7) or first_card == second_card:
        
        if first_card == second_card:
            print('type different positions!')
            print('you typed the number ' + str(first_card) + " two times")
            print('you still have ' + str(total_tries) + " tries")
            first_card = int(input('Type here a number of a position: '))
            second_card = int(input('Type here a number of a position: '))
            total_tries -= 1
        else:
            print('between(0-7)')
            print('you still have ' + str(total_tries) + " tries")
            first_card = int(input('Type here a number of a position: '))
            second_card = int(input('Type here a number of a position: '))
            total_tries -= 1
    
    
    if numbers[first_card] == numbers[second_card]:
        
        print('you still have ' + str(total_tries) + " tries")
        
        if first_card == 0:
            cards[1] = numbers[first_card]
        elif first_card == 1:
            cards[5] = numbers[first_card]
        elif first_card == 2:
            cards[9] = numbers[first_card]
        elif first_card == 3:
            cards[13] = numbers[first_card]
        elif first_card == 4:
            cards[17] = numbers[first_card]
        elif first_card == 5:
            cards[21] = numbers[first_card]
        elif first_card == 6:
            cards[25] = numbers[first_card]
        elif first_card == 7:
            cards[29] = numbers[first_card]
                                    
        if second_card == 0:
            cards[1] = numbers[second_card]
        elif second_card == 1:
            cards[5] = numbers[second_card]
        elif second_card == 2:
            cards[9] = numbers[second_card]
        elif second_card == 3:
            cards[13] = numbers[second_card]
        elif second_card == 4:
            cards[17] = numbers[second_card]
        elif second_card == 5:
            cards[21] = numbers[second_card]
        elif second_card == 6:
            cards[25] = numbers[second_card]
        elif second_card == 7:
            cards[29] = numbers[second_card]

        for element in cards:
            print(element,end=' ')
        print('')
    
    elif numbers[first_card] != numbers[second_card]:
        
        print('you still have ' + str(total_tries) + " tries")
        
        if first_card == 0:
            cards[1] = numbers[first_card]
        elif first_card == 1:
            cards[5] = numbers[first_card]
        elif first_card == 2:
            cards[9] = numbers[first_card]
        elif first_card == 3:
            cards[13] = numbers[first_card]
        elif first_card == 4:
            cards[17] = numbers[first_card]
        elif first_card == 5:
            cards[21] = numbers[first_card]
        elif first_card == 6:
            cards[25] = numbers[first_card]
        elif first_card == 7:
            cards[29] = numbers[first_card]
                                    
        if second_card == 0:
            cards[1] = numbers[second_card]
        elif second_card == 1:
            cards[5] = numbers[second_card]
        elif second_card == 2:
            cards[9] = numbers[second_card]
        elif second_card == 3:
            cards[13] = numbers[second_card]
        elif second_card == 4:
            cards[17] = numbers[second_card]
        elif second_card == 5:
            cards[21] = numbers[second_card]
        elif second_card == 6:
            cards[25] = numbers[second_card]
        elif second_card == 7:
            cards[29] = numbers[second_card]
        
        for element in cards:
            print(element, end=' ')
        print("")
    
        if first_card == 0:
            cards[1] = "_"
        elif first_card == 1:
            cards[5] = "_"
        elif first_card == 2:
            cards[9] = "_"
        elif first_card == 3:
            cards[13] = "_"
        elif first_card == 4:
            cards[17] = "_"
        elif first_card == 5:
            cards[21] = "_"
        elif first_card == 6:
            cards[25] = "_"
        elif first_card == 7:
            cards[29] = "_"
                                    
        if second_card == 0:
            cards[1] = "_"
        elif second_card == 1:
            cards[5] = "_"
        elif second_card == 2:
            cards[9] = "_"
        elif second_card == 3:
            cards[13] = "_"
        elif second_card == 4:
            cards[17] = "_"
        elif second_card == 5:
            cards[21] = "_"
        elif second_card == 6:
            cards[25] = "_"
        elif second_card == 7:
            cards[29] = "_"
        
        for element in cards:
            print(element, end=' ')
        print("")



'''   elif first_card == second_card:
        print('type different positions!')
        print('you typed the number ' + str(first_card) + " two times")
        first_card = int(input('Type here a number of a position: '))
        second_card = int(input('Type here a number of a position: '))
    
    elif (0 < first_card > 7) or (0 < second_card > 7):
        print('between(0-7)')
        first_card = int(input('Type here a number of a position: '))
        second_card = int(input('Type here a number of a position: '))
'''