my_list = [1, 72, 23, 4, 5, 6, 7, 8, 9, 10]
cnt = 1
maximum = my_list[0]
while cnt < len(my_list):
    if my_list[cnt] > maximum:
        maximum = my_list[cnt]
    cnt += 1

print(maximum)