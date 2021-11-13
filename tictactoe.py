import logging
import math
import random
from typing import List, Optional, Tuple, Union

"""
Play Tic Tac Toe with a computer that is based on the minimax algorithm.
"""

# comment out basicConfig to disable logging information
logging.basicConfig(format='%(levelname)-5s [%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

BLANK = 0
HUMAN = -1
COMP = 1
board = [[BLANK for _ in range(3)] for _ in range(3)]
player_action = {f"{i*3+j+1}":(i,j) for i in range(3) for j in range(3)}

def is_valid_move(location: Optional[Tuple[int, int]]):
    """
    A move is valid if the chosen cell is empty

    :param location: row and col in a tuple. Can accept None
    :return: True if the board[x][y] is empty
    """
    return location in empty_square()

def empty_square() -> List[Tuple[int, int]]:
    """
    Each empty square will be added into location list

    :return: a list of locations (tuple)
    """
    locations = []

    for x, row in enumerate(board):
        for y, square in enumerate(row):
            if square == BLANK:
                locations.append((x, y))

    return locations

def is_win(player: int):
    """
    Checks horizontal, vertical, diagonal if player wins

    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],

        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],

        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_state

def game_over():
    """
    End game loop
    """
    return is_win(HUMAN) or is_win(COMP)

def move(player: int, location: Tuple[int, int]) -> bool:
    """
    Place move on board, if the location is valid

    :param player: the current player
    :param location: location of move
    :return: True if move is successfully placed
    """
    row, col = location
    if is_valid_move(location):
        board[row][col] = player
        return True
    else:
        return False

def human_turn(human_icon: str, ai_icon: str):
    """
    Sanitise human input and attempts to move

    :param human_icon: the icon to be placed on board
    """
    logger.debug("human turn")
    location: Optional[Tuple[int, int]] = None

    # take input from player until valid move is given
    while not is_valid_move(location):
        try:
            location = player_action.get(input("Move [1-9]? "))
            if not is_valid_move(location):
                print("Invalid move.")
        except KeyboardInterrupt:
            print("\nExit tictactoe")
            exit()

    logger.debug(f"Player move: {location}")

    move(HUMAN, location)
    print_board(human_icon, ai_icon)

def ai_turn_random(human_icon: str, ai_icon: str):
    """
    Randomly places
    """
    logger.debug("ai turn") 

    location = random.choice(empty_square())
    move(COMP, location)
    print_board(human_icon, ai_icon)

def ai_turn(ai_icon: str):
    # rmb deep copy list before calling minimax
    depth = len(empty_square())
    move = minimax(board, depth, COMP)
    print(move)

def evaluate():
    pass 

def minimax(state, depth: int, player: int):
    """
    AI function that choice the best move

    :param state: current state of the board
    :param depth: how many moves ahead to search
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -math.inf]
    else:
        best = [-1, -1, +math.inf]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for possible_move in empty_square():
        x, y = possible_move[0], possible_move[1]
        # try move on board
        state[x][y] = player
        score = minimax(state, depth - 1, -player)

        # reset state to original
        state[x][y] = 0
        # remember moves 
        score[0], score[1] = x, y

        # only update if current move better than previous move 
        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value
    return best

def print_board(human_icon: str, ai_icon: str):
    """
    Pretty print board
    """
    chars = {
        -1: human_icon,
        +1: ai_icon,
        0: ' '
    }
    print(board)
    for row in board:
        for i in range(len(row)): 
            print(f" {chars[row[i]]} " + ("" if i == len(row) - 1 else "|"), end="")
        print()


def main():
    """Main game logic here"""
    human_icon, ai_icon = human_choose_icon()
    logger.debug(f"Human: {human_icon} AI: {ai_icon}")

    human_start_first = human_choose_start_first()
    logger.debug(f"First: {'Human' if human_start_first == 'Y' else 'AI'}")
    
    # while there is still empty squares left in board
    while len(empty_square()) != 0:
        if human_start_first == "Y":
            human_turn(human_icon, ai_icon)
            if game_over():
                break
            human_start_first= ""

        ai_turn_random(human_icon, ai_icon)
        if game_over():
                break

        human_turn(human_icon, ai_icon)
        if game_over():
                break

    game_over_message()
    

def human_choose_icon():
    """
    Lets human choose icon

    :return: tuple containing (human_icon, ai_icon)
    """
    human_icon = ""
    ai_icon = ""

    while human_icon != "X" and human_icon != "O":
        try:
            human_icon = input("X or O: ").upper() 
        except KeyboardInterrupt:
            print("\nExit tictactoe") 
            exit() 
    ai_icon = "O" if human_icon == "X" else "X"
    return human_icon, ai_icon

def human_choose_start_first():
    """
    Let human start first by choice
    
    :return: "Y" if human first, "N" if human second
    """
    human_start_first = ""

    while human_start_first != "Y" and human_start_first != "N":
        try:
            human_start_first = input("Start first? [y/n] ").upper()
        except KeyboardInterrupt:
            print("\nExit tictactoe") 
            exit()  
    return human_start_first

def game_over_message():
    """
    Handle displaying of game over message
    """

    if is_win(HUMAN):
        print("YOU WIN")
    elif is_win(COMP):
        print("AI WINS") 
    else:
        print("DRAW") 

def test():
    ai_turn("X") 

if __name__ == "__main__":
    main()
    # test()