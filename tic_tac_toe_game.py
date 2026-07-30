xo = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def display(row, col, val):
    xo[row][col] = val

    print("---+---+---")
    print(f" {xo[0][0]} | {xo[0][1]} | {xo[0][2]}")
    print("---+---+---")
    print(f" {xo[1][0]} | {xo[1][1]} | {xo[1][2]}")
    print("---+---+---")
    print(f" {xo[2][0]} | {xo[2][1]} | {xo[2][2]}")
    print("---+---+---")


def row_in():
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            if row < 0 or row > 2:
                raise ValueError
            return row
        except:
            print("Row must be between 0 and 2.")


def col_in():
    while True:
        try:
            col = int(input("Enter column (0-2): "))
            if col < 0 or col > 2:
                raise ValueError
            return col
        except:
            print("Column must be between 0 and 2.")


def o_turn():
    while True:
        print("Player O's turn")
        row = row_in()
        col = col_in()

        if xo[row][col] == '':
            display(row, col, 'O')
            return

        print("That position is already occupied. Try again.")


def x_turn():
    while True:
        print("Player X's turn")
        row = row_in()
        col = col_in()

        if xo[row][col] == '':
            display(row, col, 'X')
            return

        print("That position is already occupied. Try again.")


def winner(player):
    for i in range(3):
        if xo[i][0] == xo[i][1] == xo[i][2] == player:
            return True
    for i in range(3):
        if xo[0][i] == xo[1][i] == xo[2][i] == player:
            return True
    if xo[0][0] == xo[1][1] == xo[2][2] == player:
        return True

    if xo[0][2] == xo[1][1] == xo[2][0] == player:
        return True
    return False


def board_full():
    for row in xo:
        if '' in row:
            return False
    return True


def main():
    print("Welcome to Tic-Tac-Toe!")
    display(0, 0, '')  

    while True:
        o_turn()
        if winner('O'):
            print("🎉 Player O wins!")
            break
        if board_full():
            print("It's a draw!")
            break
        x_turn()
        if winner('X'):
            print("🎉 Player X wins!")
            break
        if board_full():
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()