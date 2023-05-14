# 2D lists are used in machine learning and in data science 

the_matrix = [
    [1, 2, 3],
    [2, 8, 3,7],
    [8, 2, 5], 
    [2, 7, 2, 3]
]

print(the_matrix[0][2])

the_matrix[2][1] = 66
print(the_matrix)

for row in the_matrix:
    for item in row:
        print(item)