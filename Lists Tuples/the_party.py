best_friends = ['Alex', 'Denis', 'Irene']

guested_friends = ['Jim', 'Bob', 'Alex', 'Maria', 'George', 'Giannis', 'Kim', 'Brian', 'lucian', 'brand']

cnt = 0
for friends in best_friends:
    if friends in guested_friends:
        cnt += 1

if cnt < 2:
    print("i won't come")

else:
    print('i will come')
    