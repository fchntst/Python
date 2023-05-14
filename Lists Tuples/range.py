# print all the evens numbers from 10 to 20 (ascending order)
for numbers in range(10,21 + 1,2):
    print(numbers)

print('--------------------')
# print all the odds numbers from 19 to 11 (descending order)
for numbers in range(19,11 - 1,-2):
    print(numbers)

print('--------------------')
# print all the numbers which are multiplied by 3 
for numbers in range(1,29 + 1,2):
    if numbers % 3 == 0:
        print(numbers)
