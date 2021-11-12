import logging
import math
import random
from copy import deepcopy
from typing import List, Optional, Tuple, Union

# comment out basicConfig to disable logging information
logging.basicConfig(format='%(levelname)-5s [%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

BLANK = "."
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

def is_win(player: str):
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

def game_over(human_icon, ai_icon):
    """
    End game loop
    """
    return is_win(human_icon) or is_win(ai_icon)

def move(player: str, location: Tuple[int, int]) -> bool:
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

def human_turn(human_icon: str):
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

    move(human_icon, location)
    print_board()

def ai_turn_random(ai_icon: str):
    """
    Randomly places
    """
    logger.debug("ai turn") 

    location = random.choice(empty_square())
    move(ai_icon, location)
    print_board()

def ai_turn(ai_icon: str):
    # rmb deep copy list before calling minimax
    board_copy = deepcopy(board)
    minimax(board_copy) 


def minimax(board_copy, depth: int, maximizingPlayer: bool):
    """
    Minimax algorithm

    :param board: board copy 
    :param depth: node index in the tree (0 <= depth <= 9)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    pass


def print_board():
    """
    Pretty print board
    """
    for i in board:
        print(i)

def main():
    """Main game logic here"""
    human_icon = ""
    ai_icon = ""
    human_start_first = ""

    # take human choice of icon 
    while human_icon != "X" and human_icon != "O":
        try:
            human_icon = input("X or O: ").upper() 
        except KeyboardInterrupt:
            print("\nExit tictactoe") 
            exit()
    ai_icon = "O" if human_icon == "X" else "X"
    logger.debug(f"Human: {human_icon} AI: {ai_icon}")

    # # human start first or second 
    while human_start_first != "Y" and human_start_first != "N":
        try:
            human_start_first = input("Start first? [y/n] ").upper()
        except KeyboardInterrupt:
            print("\nExit tictactoe") 
            exit() 
    logger.debug(f"First: {'Human' if human_start_first == 'Y' else 'AI'}")
    
    # while there is still empty squares left in board
    while len(empty_square()) != 0:
        if human_start_first == "Y":
            human_turn(human_icon)
            if game_over(human_icon, ai_icon):
                break
            human_start_first= ""

        ai_turn_random(ai_icon)
        if game_over(human_icon, ai_icon):
                break

        human_turn(human_icon)
        if game_over(human_icon, ai_icon):
                break
    
    # game over message
    if is_win(human_icon):
        print("YOU WIN")
    elif is_win(ai_icon):
        print("AI WINS") 
    else:
        print("DRAW")

def test():
    ai_turn("X") 

if __name__ == "__main__":
    # main()
    test()