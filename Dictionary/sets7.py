a = {1, 2, 3, 4}
b = {4, 5}
print('----------------------------------')
print('union = ενωση ' + str(a | b))
print('intersect = δομη ' + str(a & b))
print('difference = διαφορα ' + str(a - b))
print('difference = διαφορα ' + str(b - a))
print('symetric difference = συμετρικη διαφορα ' + str(a ^ b))
print('a subset b = α υποσυνολο β ' + str(a.issubset(b)))
print('a, b disjoint ' + str(a.isdisjoint(b)))

a.update(b)
print('a = a | b ' + str(a))
a.intersection_update(b)
print('a = a & b ' + str(a))
print('-------------------------------')