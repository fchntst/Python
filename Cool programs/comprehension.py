my_list = []
for i in range(3):
     my_list.append(i)

print(my_list)

# or we can do:

my_list = [number ** 2 for number in range(4)]
print(my_list)

my_tuple = ['Hello' for number in range(4)]
print(my_tuple)