active = True
while active:
    answer = input("type here a string or 'quit': ")
    if answer == "quit":
        print("bye bye!")
        active = False
    else:
        print("why " + answer + "?!")
