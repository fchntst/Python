from random import seed
from random import randrange
from datetime import datetime 

seed(datetime.now())

dictionary = {}

for key in range(1, 6 + 1):
    dictionary[key] = 0
print(dictionary)

for i in range(1000000):
    x = randrange(1, 6 + 1)
    dictionary[x] += 1
print(dictionary)

