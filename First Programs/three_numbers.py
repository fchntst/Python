# three numbers which one of them is the biggest
number1 = int(input('type here the first number: '))
number2 = int(input('type here the second number: '))
number3 = int(input('type here the third number: '))

maximum = number1 
if number1 < number2:
    maximum = number2
if number2 < number3:
    maximum = number3

print(maximum)
