number = int(input("type here a number between 0 and 9: "))
while number < 0 or number > 9:
    number = int(input("between 0 and 9 please: "))

print("you entered: " + str(number))