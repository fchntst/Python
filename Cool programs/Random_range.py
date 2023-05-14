from random import seed
from random import randrange
from datetime import datetime 

seed(datetime.now()) # once before randint call

x = randrange(10, 20) # from 10 to 19
print(x)
