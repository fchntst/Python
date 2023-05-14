N = 100
evens = set()
for number in range(0, N + 1):
    if number % 2 == 0:
        evens.add(number)
print(evens)
print("=====================================")

odds = set()
for number in range(0, N + 1):
    if number % 2 == 1:
        odds.add(number)
print(odds)
print("=====================================")

multi_of_3 = set()
for number in range(0, N + 1):
    if number % 3 == 0:
        multi_of_3.add(number)
print(multi_of_3)
print("=====================================")

primes = set()
for number in range(2, N + 1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        primes.add(number)
print(primes)
print("=====================================")
evens_multi_3 = set()
for number in range(0, N + 1):
    if number % 2 == 0 or number % 3 == 0:
        evens_multi_3.add(number)
print(evens_multi_3)

set1 = evens | multi_of_3
print(set1)
print("=====================================")

set2 = odds & primes
print(set2)
print("=====================================")

set3 = primes - odds
print(set3)
print("=====================================")

set4 = (primes ^ odds)
print(set4)
