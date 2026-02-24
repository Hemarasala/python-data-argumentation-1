import math

X = 'X'
O = 'O'
EMPTY = ' '
BOARD_SIZE = 3
X_WIN = 1
O_WIN = -1
DRAW = 0

def utility(board):
    for i in range(BOARD_SIZE):
        if all([board[i][j] == X for j in range(BOARD_SIZE)]):
            return X_WIN
        if all([board[i][j] == O for j in range(BOARD_SIZE)]):
            return O_WIN
        if all([board[j][i] == X for j in range(BOARD_SIZE)]):
            return X_WIN
        if all([board[j][i] == O for j in range(BOARD_SIZE)]):
            return O_WIN

    if all([board[i][i] == X for i in range(BOARD_SIZE)]):
        return X_WIN
    if all([board[i][i] == O for i in range(BOARD_SIZE)]):
        return O_WIN
    if all([board[i][BOARD_SIZE - i - 1] == X for i in range(BOARD_SIZE)]):
        return X_WIN
    if all([board[i][BOARD_SIZE - i - 1] == O for i in range(BOARD_SIZE)]):
        return O_WIN

    if all([cell != EMPTY for row in board for cell in row]):
        return DRAW

    return None

def count_Xn_On(board):
    X1, X2, X3 = 0, 0, 0
    O1, O2, O3 = 0, 0, 0

    def count_X_O(line):
        x_count = line.count(X)
        o_count = line.count(O)
        return x_count, o_count

    for row in board:
        x_count, o_count = count_X_O(row)
        if o_count == 0:
            if x_count == 1:
                X1 += 1
            elif x_count == 2:
                X2 += 1
            elif x_count == 3:
                X3 += 1
        if x_count == 0:
            if o_count == 1:
                O1 += 1
            elif o_count == 2:
                O2 += 1
            elif o_count == 3:
                O3 += 1

    for col in range(BOARD_SIZE):
        line = [board[row][col] for row in range(BOARD_SIZE)]
        x_count, o_count = count_X_O(line)
        if o_count == 0:
            if x_count == 1:
                X1 += 1
            elif x_count == 2:
                X2 += 1
            elif x_count == 3:
                X3 += 1
        if x_count == 0:
            if o_count == 1:
                O1 += 1
            elif o_count == 2:
                O2 += 1
            elif o_count == 3:
                O3 += 1

    diag1 = [board[i][i] for i in range(BOARD_SIZE)]
    diag2 = [board[i][BOARD_SIZE - i - 1] for i in range(BOARD_SIZE)]

    for diag in [diag1, diag2]:
        x_count, o_count = count_X_O(diag)
        if o_count == 0:
            if x_count == 1:
                X1 += 1
            elif x_count == 2:
                X2 += 1
            elif x_count == 3:
                X3 += 1
        if x_count == 0:
            if o_count == 1:
                O1 += 1
            elif o_count == 2:
                O2 += 1
            elif o_count == 3:
                O3 += 1

    return X1, X2, X3, O1, O2, O3

def eval_function(board):
    X1, X2, X3, O1, O2, O3 = count_Xn_On(board)
    if X3 > 0:
        return X_WIN
    if O3 > 0:
        return O_WIN

    return (3 * X2 + X1) - (3 * O2 + O1)

def minimax(board, depth, is_maximizing):
    result = utility(board)
    if result is not None:
        return result

    if is_maximizing:
        best_value = -math.inf
        for move in available_moves(board):
            board[move[0]][move[1]] = X
            value = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = EMPTY
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = math.inf
        for move in available_moves(board):
            board[move[0]][move[1]] = O
            value = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = EMPTY
            best_value = min(best_value, value)
        return best_value

def available_moves(board):
    moves = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves

def find_best_move(board, is_maximizing):
    best_value = -math.inf if is_maximizing else math.inf
    best_move = None

    for move in available_moves(board):
        board[move[0]][move[1]] = X if is_maximizing else O
        value = minimax(board, 0, not is_maximizing)
        board[move[0]][move[1]] = EMPTY

        if (is_maximizing and value > best_value) or (not is_maximizing and value < best_value):
            best_value = value
            best_move = move

    return best_move

def print_board(board):
    for row in board:
        print(' | '.join(row))
    print()

board = [
    ['X', 'O', 'X'],
    ['O', 'X', ' '],
    [' ', ' ', 'O']
]

print("Initial Board:")
print_board(board)

best_move = find_best_move(board, True)
if best_move:
    print(f"Best move for X: {best_move}")
else:
    print("Game Over!")

board[best_move[0]][best_move[1]] = X
print("Updated Board:")
print_board(board)