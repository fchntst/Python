# DUNAMIKI KATASKEUH TUPLES

my_list = []
cnt = 0
for number in range(10):
    cnt += 1
    if cnt == 1:
        user_input = int(input("give " + str(cnt) + "st number: "))

    elif cnt == 2:
        user_input = int(input("give " + str(cnt) + "nd number: "))

    elif cnt == 3:
        user_input = int(input("give " + str(cnt) + "rd number: "))

    else:
        user_input = int(input("give " + str(cnt) + "th number: "))

    while user_input < 10 or user_input > 20:
        user_input = int(input("Give a number (10...20): "))
    my_list.append(user_input)

print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
list_squares = []
for number in range(10):
    list_squares.append(my_list[number] ** 2)

list_squares.sort()
tuple_squares = tuple(list_squares)
print(tuple_squares)




