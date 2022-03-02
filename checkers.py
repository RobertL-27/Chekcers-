def red_normal(matrix, col, row):
    while True:
        col = int(col)
        row = int(row)
        if matrix[col][row] != "r ":
            print("That is not yor piece. Please choose a different collum and row: ")
            col = input()
            row = input()
        else:
            break

    while True:
        print("Choose where you would like to place your piece")
        y = input()
        x = input()
        y = int(y)
        x = int(x)
        if matrix[y][x] != matrix[col - 1][row + 1]:
            if matrix[y][x] != matrix[col - 1][row - 1]:
                print("That is not a valid spot. Please choose another spot: ")
            else:
                break
        else:
            break

    if matrix[y][x] == matrix[col - 1][row + 1]:
        if matrix[y][x] == "b ":
            matrix[y][x] = "0 "
            matrix[y - 1][x + 1] = "r "
        else:
            matrix[y][x] = "r "
            matrix[col][row] = "0 "
    else:
        if matrix[y][x] == "b ":
            matrix[y][x] = "0 "
            matrix[y - 1][x - 1] = "r "
            matrix[col][row] = "0 "
        else:
            matrix[y][x] == "r "
            matrix[col][row] = "0 "

    return matrix


def black_normal(matrix, col, row):
    col = int(col)
    row = int(row)
    while True:
        if matrix[col][row] != "b ":
            print("That is not your piece. Please choose a different collum and row: ")
            col = input()
            row = input()
        else:
            break

    while True:
        print("Choose where you would like to place your piece")
        y = input()
        x = input()
        y = int(y)
        x = int(x)
        if matrix[y][x] != matrix[col + 1][row - 1]:
            if matrix[y][x] != matrix[col + 1][row + 1]:
                print("That is not a valid spot. Please choose another spot: ")
            else:
                break
        else:
            break
    if matrix[y][x] == matrix[col + 1][row + 1]:
        if matrix[y][x] == "r ":
            matrix[y][x] = "0 "
            matrix[y + 1][x + 1] = "b "
            matrix[col][row] = "0 "
        else:
            matrix[y][x] = "b "
            matrix[col][row] = "0 "
    else:
        if matrix[y][x] == "r ":
            matrix[y][x] = "0 "
            matrix[y + 1][x - 1] = "b "
            matrix[col][row] = "0 "
        else:
            matrix[y][x] = "r "
            matrix[col][row] = "0 "

    return matrix


def main():
    board = [], []
    board = [
        ["0 ", "b ", "0 ", "b ", "0 ", "b ", "0 ", "b "],
        ["b ", "0 ", "b ", "0 ", "b ", "0 ", "b ", "0 "],
        ["0 ", "b ", "0 ", "b ", "0 ", "b ", "0 ", "b "],
        ["0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 "],
        ["0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 "],
        ["r ", "0 ", "r ", "0 ", "r ", "0 ", "r ", "0 "],
        ["0 ", "r ", "0 ", "r ", "0 ", "r ", "0 ", "r "],
        ["r ", "0 ", "r ", "0 ", "r ", "0 ", "r ", "0 "],
    ]

    while True:
        print(" ", end="")
        for a in range(8):
            print(a, " ", end="")
        print("\n")
        for i in range(8):
            print(i, " ", end="")
            for h in range(8):
                print(board[i][h], end="")
            print("\n")

        y = 0
        x = 0
        print("Red please enter the column and the row for the piece you wish to move")
        y = input()
        x = input()
        red_normal(board, y, x)
        for i in range(8):
            for h in range(8):
                if board[i][h] == "b ":
                    counter = True

        if counter != True:
            print("Red has won")
            exit()

        for i in range(8):
            for h in range(8):
                print(board[i][h], end="")
            print("\n")
        y = 0
        x = 0
        print(
            "Black please enter the column and the row for the piece you wish to move"
        )
        y = input()
        x = input()
        black_normal(board, y, x)

        for i in range(8):
            for h in range(8):
                if board[i][h] == "r ":
                    counter = True

        if counter != True:
            print("Black has won")
            exit()


if __name__ == "__main__":
    main()
