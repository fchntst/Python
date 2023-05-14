numbers = [1, 8, 7, 3, 11, 12, 9, 2, 0]
search = 2
for number in numbers: 
    print(number)
    if number == search:
        print('found it!')
        break
else:
    print('did not find it')
