# finding the first number 
user_input = int(input('give a positive number: '))
while user_input < 0:
    print("It's not a positive number!")
    user_input = int(input('give a positive number: '))

if user_input == 0 or user_input == 1:
    print("It's not prime")
else:
    for i in range(2, user_input):
        if user_input % i  == 0:
            print('it is not a prime')
            break
    else:
        print('it is prime')    
