N = 7
my_list = [number for number in range(1, N + 1)]
A = set(my_list)
print(A)

result = set()

for element in range(1, N + 1):
    my_tuple = (element, element ** 2)
    result.add(my_tuple)
    print(my_tuple, end=",")
print('')
print(result)

