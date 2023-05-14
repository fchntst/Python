# in lists we have positions and indexes we care about the sequence
# in lists we sart counting from 0 

empty_list = []

my_list = [1, 2, 3.5, True, 'thanos']
print(my_list)
print(type(my_list))
my_list[0] = 9   # element of a list
my_list[1] = 'hello world'
print(my_list)
print(my_list[4])

print('---------------------------------------------------')

# access to the elements of a list
my_list1 = [1, 2, 3, 4, 5, 6]  # if we count from left to right then we start with 0
print(my_list1[1])             # if we count from right to left then we start with -1
my_list1[-3] = 66
print(my_list1)                # if we put an index out of the range of a list it returns error

# part of a list 
# $ list_name[S:F] $ -> it returns from S position to F - 1
# $ list_name[S:] $ -> it returns from S position to the end
# $ list_name[:F] $ -> it returns all the element from the start to F - 1
# $ list_name[:] $ -> it returns all the list 
# $ list_name[-S:-F] $ it returns from -S to -F + 1

my_list2 = ["a", "b", "c", "d", "e"]
print(my_list2[-4:-2])
print(my_list2[:])
print('--------------------------------------------------------')

# methods in lists (addition):
# $ list_name.append(element) $ it adds the element at the end of a list
# $ list_name.insert(index, element) $ it adds the element at the index position of a list
# $ list_name.extend([1, 2, 'hellol', 3 ]) $ it appends the new list at the end of a list

# methods in lists (subtraction):
# $ list_name.pop(index) $ it deletes the element of the index position
# $ list_name.remove(value) $ it removes the element of value of a list
# $ list_name.clear() $ it removes all elements of a list


# existence of an element 
# ELEMENT in list: it returns T/F
# ELEMENT NOT in list: it returns T/F

# and more methods and functionalities in lists
# the function $ len(LIST) $ it returns the length of a list
# the function $ LIST.sort() $ it sorts the data
# the function $ LIST.reserve() $ it reserves all the data
