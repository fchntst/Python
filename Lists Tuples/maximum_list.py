# Trying to find the max number in the list with repetition

my_numbers = [1, 6, 3, 67, 23, 1, 4, 9, 23, 7]
maximum = my_numbers[0] 
i = 0 
while i <= 8:
    i += 1
    if my_numbers[i] > maximum:
        maximum = my_numbers[i]     

print(maximum)

# i tried to make the program with successfully failure 
# so i took some help from youtube