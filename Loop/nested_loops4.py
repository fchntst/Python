n = 5 
for i in range(0, n):
    for j in range(0, n - i):
        print(" ", end=" ")
    for j in range(0, 2 * i):
        print("*", end=" ")    
    print('')

