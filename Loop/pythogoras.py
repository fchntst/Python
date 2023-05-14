# x ** 2 + y ** 2 = z ** 2 

for x in range(1, 20 + 1):
    for y in range(1, 20 + 1):
        for z in range(1, 20 + 1):
            if x ** 2 + y ** 2 == z ** 2:
                print("(" + str(x) + "," + str(y) + "," + str(z) + ")")
