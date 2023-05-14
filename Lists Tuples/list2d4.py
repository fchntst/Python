''' οκ ηρθε η ωρα να γραψουμε λιγη 
    ποιηση γιατι καλη η python αλλα σαν
    την ποιηση δεν εχει
'''

my_list = [
    [1, 6, 4, 4],
    [2, 4, 2, 1],
    [5, 2, 9, 8]
]

my_list.insert(0, [0, 0, 0, 0])


for row in my_list:
    row.append(1)
    for element in row:
        print(element, end=' ')
    print('')