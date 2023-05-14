# two players wanna know who's gonna play first using dices
first_player = 'George'
second_player = 'Joe'

first_dice1 = int(input(first_player + ' throw the first dice: '))
first_dice2 = int(input(first_player + ' throw the second dice: '))

second_dice1 = int(input(second_player + ' throw the first dice: '))
second_dice2 = int(input(second_player + ' throw the second dice: '))

while first_dice1 > 6 or first_dice2 > 6 or second_dice1 > 6 or second_dice2 > 6:
    print('between 1 to 6 please!')
    first_dice1 = int(input(first_player + ' throw the first dice: '))
    first_dice2 = int(input(first_player + ' throw the second dice: '))
    
    second_dice1 = int(input(second_player + ' throw the first dice: '))
    second_dice2 = int(input(second_player + ' throw the second dice: '))

if first_dice1 + first_dice2 > second_dice1 + second_dice2:
    print(first_player + " plays first.")

elif first_dice1 + first_dice2 < second_dice1 + second_dice2:
    print(second_player + " plays first.")

elif first_dice1 + first_dice2 == second_dice1 + second_dice2:
    print("throw them again!")
    