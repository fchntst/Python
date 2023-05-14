my_list = []
for number in range(20 + 1):
   if number % 2 == 0:
       my_list.append(number)
print(my_list)

# or we can do comprehension

my_list = [number for number in range(20 + 1) if number %  2 == 0]
print(my_list)
