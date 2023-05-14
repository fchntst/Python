program = True
my_numbers = []
insert = 1

while program and insert <= 10:
    number = int(input('"quit" or insert no' + str(insert) + " number: "))
    if number != "quit":
        my_numbers.append(number)
        print(my_numbers)
        insert += 1
    else:
        program = False

Sum = sum(my_numbers)
print("result is : " + str(Sum) + " bye bye")
program = False