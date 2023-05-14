# Program that calculates the square of a number 

number = input("type here a number or quit: ")

while number != 'quit':
    number1 = int(number) ** 2
    print("the square number is: " + str(number1))
    number = input("type here a number or quit: ")

print('you ended the program')

