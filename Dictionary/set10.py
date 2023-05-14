my_set = set()
for i in range(2):
    for j in range(3):
        my_set.add((i, j))
print(my_set)

# or the same code:

my_set1 = {(i, j) for i in range(2)
           for j in range(3)}
print(my_set1)