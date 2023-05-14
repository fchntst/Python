my_list = []

for numbers in range(2, 101):
    for i in range(2, numbers):
        if numbers % i == 0:
            break

    else:
        my_list.append(numbers)

print(tuple(my_list))

