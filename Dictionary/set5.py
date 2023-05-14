N = 5  # αρχηκοποίηση
A = set()
for number in range(1, N + 1):
    A.add(number)
print(A)

result = set()
for element in A:
    result.add((element, element ** 2))

print(result)