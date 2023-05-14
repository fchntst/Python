# add all the numbers with the while in a list
list_numbers = [10, 4, 43, 2, 23, 72, 5, 2, 1, 76]
i = 1
addition = 0 
while i <= 10: 
    addition += list_numbers[i - 1]
    i += 1
print("the sum is: " + str(addition))

