# tuples or lists or aka sequences

my_tuple = (1, 0, 3, 43, 5, -6, 7, 8, 9, 2, 5, 2)
my_tuple1 = ('hi', True)
my_tuple2 = ('thanos',)

print(my_tuple + 2 * my_tuple1 + my_tuple2 * 4)


maximum = max(my_tuple)
print(maximum)
minimum = min(my_tuple)
print(minimum)

print(len(my_tuple))

ii = my_tuple.count(2)
print(ii)

uu = my_tuple.index(5)

print(uu)
