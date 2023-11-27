"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_number,o_number,empty_number = number_of_values(board)
    if empty_number == 9 or o_number == x_number:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for index_i, i in enumerate(board):
        for index_j,j in enumerate(i):
            if j == EMPTY:
                actions.append((index_i,index_j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if (action[0] > len(board) or action[1] > len(board[action[0]])) or board[action[0]][action[1]] != EMPTY:
        raise Exception("Action not allowed")
    player_move = player(board)
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player_move
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board != None:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != None:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]
    return None  
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    _,_,empty_number = number_of_values(board)
    if empty_number == 0 or winner(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    x_number,o_number,empty_number = number_of_values(board)
    if o_number == x_number:
        return max_value(board)[0]
        
    return min_value(board)[0]


def max_value(board):
    score_max = -math.inf
    if terminal(board):
        return None,utility(board)
    actions_list = actions(board)
    scores = []
    for action in actions_list:
        scores.append(min_value(result(board, action))[1])
    score_max = max(scores)
    return actions_list[scores.index(score_max)], score_max

def min_value(board):
    score_min = math.inf
    if terminal(board):
        return None,utility(board)
    actions_list = actions(board)
    scores = []
    for action in actions_list:
        scores.append(max_value(result(board, action))[1])
    score_min = min(scores)
    return actions_list[scores.index(score_min)], score_min
           

def number_of_values(board):
    """
        Returns the number of X , O or EMPTY values in the board
    """
    x_number = 0
    o_number = 0
    empty_number = 0
    for i in board:
        for j in i:
            if j == X:
                x_number+= 1
            elif j == O:
                o_number += 1
            else:
                empty_number += 1
    return (x_number,o_number,empty_number)
    