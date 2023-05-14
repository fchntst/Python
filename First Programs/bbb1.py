cnt = 1
s = 0

while cnt <= 10:
    number = int(input("give " + str(cnt) + " th number: "))
    cnt = cnt + 1
    s = s + cnt

print("the sum is: " + str(s))
