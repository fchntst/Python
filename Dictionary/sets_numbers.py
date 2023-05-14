my_even = set()

for number in range(100 + 1):
    if number % 2 == 0:
        my_even.add(number)
print(my_even)

print('-------------------')

my_odds = set()
for number in range(100 + 1):
    if number % 2 != 0:
        my_odds.add(number)

print(my_odds)

print('-------------------')

three_multi = set()
for number in range(100 + 1):
    if number % 3 == 0:
        three_multi.add(number)

print(three_multi)
print('--------------------')

primes = set()            # den katalavainw tipota edw 
for number in range(2, 100 + 1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        primes.add(number)

print(primes)
print('------------------------------')

even_threeMulti = set()
even_threeMulti = my_even.union(three_multi)
print(even_threeMulti)
print('--------------------')

odds_primes = set()
odds_primes = my_odds.intersection(primes)
print(odds_primes)
print('--------------------')

primes_no_odds = set()
primes_no_odds = primes.difference(my_odds)
print(primes_no_odds)
