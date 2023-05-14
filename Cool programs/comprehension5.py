my_list = []
for number in range(100 + 1):
    if number % 2 == 0 and number % 3 == 0:
        my_list.append(number)
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

print('s==================================================================s')

my_list = [number for number in range(100 + 1) if number % 2 == 0 and number % 3 == 0]

print(my_list)


