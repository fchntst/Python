#

my_list = []

for i in range(2, 100 + 1):
    for j in range(2, i):
        if i % j == 0:
            break
        
    else:
        my_list.append(i)

my_tuple = tuple(my_list)
print(my_tuple) 
