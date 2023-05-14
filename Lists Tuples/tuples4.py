my_list =[1, 2, 3]
new_list = ((2 * my_list)[1:5] + list((7, 8))) * 4
print(str((my_list + new_list).count(2)))
print(my_list + new_list)
