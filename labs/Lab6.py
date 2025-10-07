board = []
is_PlayerOne = True # True = Player 1, False = Player 2

height = 4
length = 4

def initialize_board(rows, columns):
    for i in range(0, columns):
        board.append([])
        for j in range(0, rows):
            board[i].append("-")

    return board

def print_board(board):
    for row in reversed(board):
        for index, column in enumerate(row):
            if index == length - 1:
                print(column)
            else:
                print(column, end=" ")

def insert_chip(board, column, chip_type):
    for row in board:
        if row[column] == "-":
            row[column] = chip_type
            break

def check_if_winner(board, column, row, chip_type):
    horizontal_counter = 0
    vertical_counter = 0

    for i in range(0, height):
        for j in range(0, length):
            if board[i][j] == chip_type:
                horizontal_counter += 1
        
        if horizontal_counter == 4:
            return True
        else:
            horizontal_counter = 0

    for i in range(0, length):
        for row in board:
            if row[i] == chip_type:
                vertical_counter += 1

        if vertical_counter == 4:
            return True
        else:
            vertical_counter = 0

    return False

def check_for_draw():
    for row in board:
        for chip in row:
            if chip == "-":
                return False
            
    return True

if __name__ == "__main__":
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))

    initialize_board(length, height)
    print_board(board)

    print("\nPlayer 1: x\nPlayer 2: o")

    while True:
        column_choice = int(input(f"\nPlayer {1 if is_PlayerOne else 2}: Which column would you like to choose? "))
        insert_chip(board, column_choice, "x" if is_PlayerOne else "o")

        if check_if_winner(board, "", "", "x" if is_PlayerOne else "o"):
            print_board(board)
            print(f"\nPlayer {1 if is_PlayerOne else 2} won the game!")
            break
        elif check_for_draw():
            print_board(board)
            print("\nDraw. Nobody wins.")
            break
        
        is_PlayerOne = not is_PlayerOne

        print_board(board)