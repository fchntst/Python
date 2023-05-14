# set is a collection without a spesific row 
# like math where you can not have two same elements, sets are also like this

empty_set = set()
int_set = {1, 2, 3}
collection = {'hi', 3.14, True}
duplicates = {1, 2, 3, 2, 1, 1, 2}
print(duplicates)
print(type(int_set))

# we expect the result of a set being randomly

print('------------------------------------------------------------------')

# action in sets:
# indexes and ranges do not exist
# but we do 
# tests: if element in set
# loops: for element in set
# a set can't contain a list cuse the list is mutable

# methods for adding an element in a set:
# $ set_name.add(element) $ it adds an element is a set  
# $ set_name.update(collection) $ 


# set copy
old_set = {1, 2, 3}
new_set = old_set.copy()
new_set.add(5)
print(new_set)

print('----------------------------------------------------------')

# methods for subtrackting an element in a set
# $ set_name.remove(element) $ it causes error if element not in set 
# usually we use the remove method
# $ set_name.discard(element) $ it does not cause an error if element not in set 
# $ set_name.pop() $ it removes an element from the set but we do not know which
# $ set_name.clear() $ it removes all the element from the set 

# conversions 
# set_name = set(collection)

