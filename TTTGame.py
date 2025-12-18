def printgb(board):
    print("Game Board:")
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
        if i < 6:
            print("----------")


def wincheck(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return 0


print("This is a Tic Tac Toe Game.")
print("The game alternates between X and O!")
print("The first user will be X. The next will be O.")
print("Play using numpad 1 to 9 as a game board.")

board = [" "] * 9
count = 0

while count < 9:
    player = "X" if count % 2 == 0 else "O"

    printgb(board)
    print(f"Player {player} turn:")

    try:
        move = int(input("Enter number from 1 to 9: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if move < 1 or move > 9:
        print("Move is out of range, try again.")
        continue

    if board[move - 1] != " ":
        print("Already occupied, try again.")
        continue

    board[move - 1] = player

    winner = wincheck(board)
    if winner:
        printgb(board)
        print(f"Player {winner} wins!")
        break

    count += 1

if count == 9 and wincheck(board) == 0:
    printgb(board)
    print("It's a draw!")

print("\nThank you for playing!")
