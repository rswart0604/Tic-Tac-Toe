# write your code here\
global finished


def instantiate_rows(input):
    for n in range(3):
        row_1.append(input[n])
    for n in range(3, 6):
        row_2.append(input[n])
    for n in range(6, 9):
        row_3.append(input[n])


def board_print(matrix):
    print("---------")
    print("|", matrix[0][0], matrix[0][1], matrix[0][2], "|")
    print("|", matrix[1][0], matrix[1][1], matrix[1][2], "|")
    print("|", matrix[2][0], matrix[2][1], matrix[2][2], "|")
    print("---------")


def check_lines(matrix):
    row_x, row_o, column_x, column_o, b_diagonal_x, b_diagonal_o, t_diagonal_x, t_diagonal_o, \
        impossible, won, spaces_present = \
        False, False, False, False, False, False, False, False, False, False, False
    x_count, o_count, space_count = 0, 0, 0
    for x in range(3):  # Check the rows
        if matrix[x] == ["X", "X", "X"]:
            row_x = True
        elif matrix[x] == ["O", "O", "O"]:
            row_o = True
    for x in range(3):  # Check the columns
        if matrix[0][x] == matrix[1][x] == matrix[2][x] == "X":
            column_x = True
        elif matrix[0][x] == matrix[1][x] == matrix[2][x] == "O":
            column_o = True
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == "X":  # Check diagonals
        b_diagonal_x = True
    elif matrix[0][0] == matrix[1][1] == matrix[2][2] == "O":
        b_diagonal_o = True
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == "X":
        t_diagonal_x = True
    elif matrix[0][2] == matrix[1][1] == matrix[2][0] == "O":
        t_diagonal_o = True
    # Check for impossibilities in the number of rows/columns
    bools = [row_x, row_o, column_x, column_o, b_diagonal_x, b_diagonal_o, t_diagonal_x, t_diagonal_o]
    n = 0
    for x in bools:
        if x:
            n += 1
    if n >= 2:
        print("Impossible")
        impossible = True
    if not impossible:  # Check for impossibilities in the number of X's and O's
        x_count, o_count, space_count = 0, 0, 0
        for x in range(3):
            for y in range(3):
                if matrix[x][y] == "X":
                    x_count += 1
                if matrix[x][y] == "O":
                    o_count += 1
                if matrix[x][y] == "_":
                    space_count += 1
        if abs(x_count - o_count) >= 2:
            print("Impossible")
            impossible = True
    # Display result if there is any
    if not impossible:
        if row_x or t_diagonal_x or b_diagonal_x or column_x:
            print("X wins")
            global finished
            finished = True
        elif row_o or t_diagonal_o or b_diagonal_o or column_o:
            print("O wins")
        elif space_count == 0:
            print("Draw")
            finished = True
        else:
            finished = False


def add_coord_to_board(matrix, turn):
    global coordinates_input
    coordinates_chosen, number_is_int = False, True
    coordinates = ["a", "b"]
    x, y = 1, 1
    while not coordinates_chosen:
        try:
            coordinates_input = list(input("Enter the coordinates: "))
        except EOFError:
            print("whoops")
            break
        if coordinates_input:
            coordinates = [n for n in coordinates_input if n != " "]
        try:
            x = int(coordinates[0])
            y = int(coordinates[1])
            number_is_int = True
        except ValueError:
            print("You should enter numbers!")
            number_is_int = False
        if 1 <= x <= 3 and 1 <= y <= 3 and number_is_int:
            if matrix[3 - y][x - 1] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                coordinates_chosen = True
        elif number_is_int:
            print("Coordinates should be from 1 to 3!")
    if turn % 2 == 0:
        matrix[3 - y][x - 1] = "X"
    elif turn % 2 == 1:
        matrix[3 - y][x - 1] = "O"


if __name__ == '__main__':
    while True:
        row_1, row_2, row_3 = ["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]
        board = [row_1, row_2, row_3]
        board_print(board)
        turn_number = 2
        while True:
            add_coord_to_board(board, turn_number)
            board_print(board)
            check_lines(board)
            if finished:
                break
            turn_number += 1
