active = True

while active:
    user_input = input('Give a string or quit: ')
    if user_input == 'quit':
        print('Bye bye!')
        active = False
    else:
        print('why ' + user_input + "?!")
        

