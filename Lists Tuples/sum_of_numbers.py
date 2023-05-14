# add all the numbers with the while

i = 1
addition = 0 
while i <= 10: 
    
    user_input = int(input('Give a number ' + str(i) + "th number: "))
    i += 1
    addition += user_input

print("the sum is: " + str(addition))



