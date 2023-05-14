# Guess the number game

print(" ")
print("""!hello! 
!-----! let's play a game,
!-----! you have to find the hidden number
!-----! you have 10 tries!
!-----! good luck """)

real_number = True
print(" ")
hidden_number = int(input("type here and try to find the number!: "))
tries = 10
cnt = 1
while real_number:
    tries -= cnt
    print(str(tries) + " tries left")

    if tries == 0:
        print("game over")
        break

    elif hidden_number == 100:
        print("well done you find the hidden number!")
        real_numb = False

    elif hidden_number <= 0:
        print("""you are way to far from the hidden number,
you have to add more numbers!""")
        hidden_number = int(input("try again: "))

    elif 0 <= hidden_number <= 60:
        print("you need to add more!")
        hidden_number = int(input("try again here: "))

    elif 60 <= hidden_number <= 90:
        print("you need to add a little more!")
        hidden_number = int(input("try again here: "))

    elif 90 <= hidden_number <= 100:
        print("you are so close! add a little bit more!")
        hidden_number = int(input("try again here: "))

    elif 100 <= hidden_number <= 110:
        print("you are so close! subtract a little bit more")
        hidden_number = int(input("try again here: "))

    elif 110 < hidden_number <= 150:
        print("you need to subtract a little more!")
        hidden_number = int(input("try again here: "))

    elif 150 <= hidden_number:
        print("""you are way to far from the hidden number,
you have to subtract more numbers!""")
        hidden_number = int(input("try again here: "))
