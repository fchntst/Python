my_set1 = {number for number in range(5)}
print(my_set1)
print('')

my_set2 = {number for number in range(5) if number % 2 == 0}
print(my_set2)
print('')

my_set3 = {number if number % 2 == 0 else number / 2
                            for number in range(10)}
print(my_set3)
print('')

my_set4 = {(i, j) for i in range(2)
                  for j in range(3)}
print(my_set4)
print('')

my_set5 = {(i, j) for i in range(5) if i % 2 == 0
                  for j in range (3) if j % 2 == 1}
print(my_set5)
print('')