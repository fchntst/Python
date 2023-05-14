# making a parallelogram with asterisks 

n = 5 
for i in range(0, n):
    print(' ' * (n - i - 1), end=' ')
    print('*' * (2 * n + 1), end=' ')
    print(' ')
