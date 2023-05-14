board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

player = "o"

for _ in range(9):
    # print board
    print("  +---+---+---+")
    print(str(2) + " | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("  +---+---+---+")
    print(str(1) + " | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("  +---+---+---+")
    print(str(0) + " | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print("    0   1   2  ")

    # choose next player
    if player == "x":
        player = "o"
    else:
        player = "x"
    # user input
    print("player " + player + " plays! ")
    while True:
        row = int(input("Give row: "))
        col = int(input("Give column: "))
        if row < 0 or row > 2:
            print("Row out of bounds, (0-2). ")
            continue
        elif col < 0 or col > 2:
            print("coloumn out of bounds, (0-2). ")
            continue
        elif board[row][col] != " ":
            print("Pick an empty box")
            continue
        else:
            board[row][col] = player
            break
# winner check
    winner = False
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2]) and board[0][0] != " ":
        winner = player
    elif (board[1][0] == board[1][1] and board[1][1] == board[1][2]) and board[1][0] != " ":
        winner = player
    elif (board[2][0] == board[2][1] and board[2][1] == board[2][2]) and board[2][0] != " ":
        winner = player
    elif (board[0][0] == board[0][1] and board[0][1] == board[0][2]) and board[0][0] != " ":
        winner = player
    elif (board[1][0] == board[1][1] and board[1][1] == board[1][2]) and board[1][0] != " ":
        winner = player
    elif (board[2][0] == board[2][1] and board[2][1] == board[2][2]) and board[2][0] != " ":
        winner = player
    elif (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != " ":
        winner = player
    elif (board[2][0] == board[1][1] and board[1][1] == board[0][2]) and board[2][0] != " ":
        winner = player

    if winner:
        print("+---+---+---+")
        print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
        print("+---+---+---+")
        print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
        print("+---+---+---+")
        print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
        print("+---+---+---+")
        print("player " + player + " won!")
        break



else:
    print("+---+---+---+")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("+---+---+---+")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("+---+---+---+")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("+---+---+---+")
    print("draw or stand-off or tie")
