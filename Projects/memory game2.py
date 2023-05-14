hidden = [2, 3, 1, 4, 3, 1, 2, 4]
N = 8

state = ["closed", "closed", "closed", "closed", "closed", "closed", "closed", "closed"]
# other states: open, temp_open

active_game = True
found = 0
score = 0
while active_game:
    score += 1
    # read first position
    first_position = int(input("Give first position (0 - 8) and closed: "))
    while (first_position < 0 or first_position >= 8) or state[first_position] == "open":
        print("Error!")
        first_position = int(input("Give first position (0 - 8) and closed: "))

    # read second position
    second_position = int(input("Give second position (0 - 8) and closed: "))
    while (second_position < 0 or second_position >= 8) or state[second_position] == "open" \
            or second_position == first_position:
        print("Error!")
        second_position = int(input("Give second position (0 - 8) and closed: "))

    # change state: both temp_open
    state[first_position] = "temp_open"
    state[second_position] = "temp_open"

    # print current state
    print("")
    for position in range(N):
        if state[position] == "closed":
            print("_", end="")
        elif state[position] == "open":
            print(hidden[position], end="")
        else:
            print(hidden[position], end="")
    print("")

    # check if same then open, else closed
    if hidden[first_position] == hidden[second_position]:
        state[first_position] = "open"
        state[second_position] = "open"
        print("Success!")
        found += 2
    else:
        state[first_position] = "closed"
        state[second_position] = "closed"
        print("Failure")

    # print current state
    print("")
    for position in range(8):
        if state[position] == "closed":
            print("_", end="")
        elif state[position] == "open":
            print(hidden[position], end="")
        else:
            print(hidden[position], end="")
    print("")

    if found == N:
        print("Well done! Game finished, Score = " + str(score))
