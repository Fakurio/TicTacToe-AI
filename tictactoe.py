"""
Tic Tac Toe Player
"""

import copy, math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if not terminal(board):
        moves = 0
        for row in range(3):
            for col in range(3):
                if board[row][col] != EMPTY:
                    moves += 1
        if moves % 2 == 0:
            return X
        return O
    return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if not terminal(board):
        actions = set()
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    actions.add((row, col))
        return actions
    return None


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError("This action is not possible")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    counter = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                counter += 1
    if counter == 0 or winner(board) is not None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        return max(board, alpha=-math.inf, beta=math.inf)[1]
    else:
        return min(board, alpha=-math.inf, beta=math.inf)[1]


def max(board, alpha, beta):
    if terminal(board):
        return [utility(board), None]

    v = -math.inf
    move = None
    for action in actions(board):
        try:
            v_prime = min(result(board, action), alpha, beta)[0]
            if v_prime > v:
                v = v_prime
                move = action
            if v_prime >= beta:
                return [v, move]
            if v_prime > alpha:
                alpha = v_prime
        except ValueError:
            continue
    return [v, move]


def min(board, alpha, beta):
    if terminal(board):
        return [utility(board), None]

    v = math.inf
    move = None
    for action in actions(board):
        try:
            v_prime = max(result(board, action), alpha, beta)[0]
            if v_prime < v:
                v = v_prime
                move = action
            if v_prime <= alpha:
                return [v, move]
            if v_prime < beta:
                beta = v_prime
        except ValueError:
            continue
    return [v, move]
