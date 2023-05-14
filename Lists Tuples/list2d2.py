array = []
rows = int(input("Give a number of rows: "))
cols = int(input('Give a number of columns: '))
for i in range(rows):
    array.append([])
    for j in range(cols):
        elem = int(input("Give " + "(" + str(i) + "," + str(j) + ")" + " elements: "))
        array[i].append(elem)

print(array)
