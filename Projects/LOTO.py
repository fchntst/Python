from random import seed
from random import randrange
from datetime import datetime 

seed(datetime.now())

for elem in range(10):
    my_set = set() 

    rand_number = randrange(10, 20)
    my_set.add(rand_number)

    while True:
        rand_number = randrange(10, 20)
        if rand_number not in my_set:
            my_set.add(rand_number)
            break


    rand_number = randrange(20, 40)
    my_set.add(rand_number)

    while True:
        rand_number = randrange(20, 40)
        if rand_number not in my_set:
            my_set.add(rand_number)
            break

    rand_number = 2 * randrange(1, 5)
    my_set.add(rand_number)

    rand_number = randrange(41, 50, 2)

    print(my_set)