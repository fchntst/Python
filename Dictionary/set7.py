A = {1, 2, 3, 4, 5, 7}
B = {1, 4, 5}
print("Union: " + str(A | B))  # union = σενένωση
print("Intersection: " + str(A & B))  # intersection = τομή
print("Diff A-B: " + str(A - B))  # difference = διαφορά
print("Diff B-A: " + str(B - A))  # difference = διαφορά
print("Symm.dif.: " + str(A ^ B))  # symmetric difference = συμετρική διαφορά
print("A subset B: " + str(A.issubset(B)))  # subset = υποσύνολο
print("A superset B: " + str(A.issuperset(B)))
print("A, B disjoint: " + str(A.isdisjoint(B)))


A.update(B)  # Union
print("A = A | B: " + str(A))
A.intersection_update(B)
print("A = A & B: " + str(A))
my_list = set()
