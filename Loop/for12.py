friends_list = ["a", "b", "c"]
guest_list = ["1", "2", "a", "4", "4", "6", "c", "8", "9", "10"]
cnt = 0
for friend in friends_list:
    if friend in guest_list:
        cnt = cnt + 1
print("friends in guest list: " + str(cnt))

if cnt < 2:
    print("i won't go to the party")
else:
    print("i'll go to the party")
