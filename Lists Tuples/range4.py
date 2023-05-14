# In this program we are gonna to sort the numbers

N = int(input('Give a number between 3 to 20: '))
while N < 3 or N > 20:
    N = int(input('between 3 to 20 please: '))
    

my_list = []

for cnt in range(0,N):
    if cnt == 0:
        my_list.append(int(input("Give " + str(cnt + 1) + "st number: ")))
    elif cnt == 1:
        my_list.append(int(input("Give " + str(cnt + 1) + "nd number: ")))
    elif cnt == 2:
        my_list.append(int(input("Give " + str(cnt + 1) + "rd number: ")))
    else:
        my_list.append(int(input("Give " + str(cnt+1) + "th number: ")))

my_list.sort()
print(my_list)

# that was a good one, i should check it in the future again
