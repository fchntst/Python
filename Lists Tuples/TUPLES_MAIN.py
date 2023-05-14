# tuple is a collection like list but with the spesific row
# the values are immutable they can't change 
# it is like a list with the only difference that lists' values are mutable\

empty_tuple = ()
tuple_of_one = (3,)   # if we do not add the comma then it's not a tuple is an integer
my_tuple = (1, 2, 3, 4)

print(my_tuple)
print(tuple_of_one)
print(type(empty_tuple))
print('-----------------------------------------------------------------------')

# treatment of a tuple:
# indexing: $ tuple_name[1] and tuple_name[-2] $ 
# checking: $ if element if tuple $
# loops: $ for element in tuple $ 

# we use tuple when we know that the elements of a collection won't change! 
# and usually we prefer to use tuples than lists

my_tuple1 = (1, 2, 3)
print(my_tuple1[1:3])
print(my_tuple1[1] + 4)
for number in my_tuple1:
    print(number, end='')

print('---------------------------------------------------------------------------')

# tuple is a sequence 
# act                               explanation
# elem in seq                       T/F
# elem not in seq                   T/F
# seq1 + seq2                       concatenation
# seq * N or N * seq                concatenation N times
# seq[i], seq[i:j], seq[i,j,k]      indexing, slicing and slicing with step
# len(seq)                          length of seq
# min(seq)                          minimum element of a seq
# man(seq)                          maximum element of a seq
# seq.index(elem, s, f)             it returns the position of the first elem in seq  (i, f are optional)
# seq.count(elem)                   it counts how many times is the elem in a seq


# usefull conversions
my_list = [1, 2, 3]
my_tuple2 = tuple(my_list)

my_tuple3 = (1, 2, 3)
my_list2 = list(my_tuple3)

my_list3 = list(range(4))
print(my_list3)

msg = 'hello'
print(list(msg))

print('------------------------------------------------------')

numbers = (1,2,3,4,3,2,3,3)
print("Length: " + str(len(numbers)))
print("min: " + str(min(numbers)))
print("max: " + str(max(numbers)))
print("3s: " + str(numbers.count(3)))
print("pos of a 3: " + str(numbers.index(3,4)))

print('-----------------------------------------------------------')

# copy a tuple 

old_list = []

new_list = old_list[:]
new_list = old_list.copy()  # the copy is a better option i would say

