my_list = []

cnt = 0

while cnt < 10:
    ii = int(input('give a number between(10 - 20): '))
    if 10 <= ii <= 20: 
        cnt += 1 
        my_list.append(ii)
    else:
        print('between(10-20) please: ')

print(my_list)

list_square = []
for ii in range(10):
    list_square.append(my_list[ii] ** 2)


list_square.sort()
tuple_square = tuple(list_square)
print(tuple_square)