old_list = [1, 2, 3]
print(old_list)
new_list = old_list.copy()
new_list[0] = 8
print(new_list)

# copy sequences

old_tuple = (1, 2, 3, 4)
print(old_tuple)
new_tuple = list(old_tuple[:])
new_tuple[1] = 9
new_tuple = tuple(new_tuple)
print(new_tuple)