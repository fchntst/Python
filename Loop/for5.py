number = int(input("give here a number between 3 and 20:"))
while number < 3 or number > 20:
    print("between 3 and 20 please!")
    number = int(input("give here again a number between 3 and 20:"))

numbers = []
for numb in range(0 + 1, number):
    if numb == 1:
        numbers.append(int(input("give " + str(numb) + "st number: ")))
    elif numb == 2:
        numbers.append(int(input("give " + str(numb) + "nd number: ")))
    elif numb == 3:
        numbers.append(int(input("give " + str(numb) + "rd number: ")))
    else:
        numbers.append(int(input("give " + str(numb) + "st number: ")))

numbers.sort()

print(numbers)




