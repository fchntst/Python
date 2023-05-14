array = [[1, 2, 3], [4, 5, 2]]

array[0][1] = 0

for row in array:
    for element in row:
        print(element, end=' ')
    print("")
