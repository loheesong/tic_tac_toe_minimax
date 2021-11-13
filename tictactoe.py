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
    return location in empty_square(board)

def empty_square(state) -> List[Tuple[int, int]]:
    """
    Each empty square will be added into location list

    :param state: current board state
    :return: a list of locations (tuple)
    """
    locations = []

    for x, row in enumerate(state):
        for y, square in enumerate(row):
            if square == BLANK:
                locations.append((x, y))

    return locations

def is_win(state, player: int):
    """
    Checks horizontal, vertical, diagonal if player wins

    :param state: current board state
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],

        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],

        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    return [player, player, player] in win_state

def game_over(state):
    """
    Check for both player winning

    :param state: current board state
    """
    return is_win(state, HUMAN) or is_win(state, COMP)

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
    :param ai_icon: computer icon for printing board
    """
    logger.debug("human_turn")
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
    Randomly places move.

    :param human_icon: human icon for printing board
    :param ai_icon: the icon to be placed on board
    """
    logger.debug("ai_turn_random") 

    location = random.choice(empty_square(board))
    move(COMP, location)
    print_board(human_icon, ai_icon)

def ai_turn_minimax(human_icon: str, ai_icon: str):
    """
    AI plays move determined by minimax algorithm.

    :param human_icon: human icon for printing board
    :param ai_icon: the icon to be placed on board 
    """
    logger.debug("ai_turn_minimax")

    depth = len(empty_square(board))
    # if AI is starting first, place in a random corner
    if depth == 9:
        move_location: tuple[int, int] = (random.choice([0,2]), random.choice([0,2]))
    else:
        move_location = tuple(minimax(board, depth, COMP)[:2])

    logger.debug(f"Move: {move_location}")

    move(COMP, move_location)
    print_board(human_icon, ai_icon)

def evaluate(state):
    """
    Evaluate current board state
    
    :param state: current board state
    :return: +1 for AI win, -1 for human win, 0 for tie
    """
    if is_win(state, COMP):
        return 1 
    elif is_win(state, HUMAN):
        return -1 
    else:
        return 0  

def minimax(state, depth: int, player: int):
    """
    Finds the best move for AI to make. COMP is maximizing while HUMAN is minimizing.

    :param state: current state of the board
    :param depth: how many moves ahead to search
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        # set best to worst possible score for maximizing player
        best = [-1, -1, -math.inf]
    else:
        # set best to worst possible score for minimizing player
        best = [-1, -1, +math.inf]

    # base case
    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for possible_move in empty_square(state):
        row, col = possible_move[0], possible_move[1]
        # try move on board
        state[row][col] = player
        score = minimax(state, depth - 1, -player)

        # reset state to original
        state[row][col] = 0
        # remember moves 
        score[0], score[1] = row, col

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
        HUMAN: human_icon,
        COMP: ai_icon,
        BLANK: ' '
    }
    print_instructions()
    for row in board:
        for i in range(len(row)): 
            print(f" {chars[row[i]]} " + ("" if i == len(row) - 1 else "|"), end="")
        print()

def print_instructions():
    """Print instructions for input"""
    print(" 1 | 2 | 3 ")
    print(" 4 | 5 | 6 ") 
    print(" 7 | 8 | 9 ") 
    print()

def main():
    """Main game logic here"""
    human_icon, ai_icon = human_choose_icon()
    logger.debug(f"Human: {human_icon} AI: {ai_icon}")

    human_start_first = human_choose_start_first()
    logger.debug(f"First: {'Human' if human_start_first == 'Y' else 'AI'}")
    
    print_board(human_icon, ai_icon)
    # while there is still empty squares left in board
    while len(empty_square(board)) != 0:
        if human_start_first == "Y":
            human_turn(human_icon, ai_icon)
            if game_over(board):
                break
            human_start_first= ""

        ai_turn_minimax(human_icon, ai_icon)
        if game_over(board):
                break

        human_turn(human_icon, ai_icon)
        if game_over(board):
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

    if is_win(board, HUMAN):
        print("YOU WIN")
    elif is_win(board, COMP):
        print("AI WINS") 
    else:
        print("DRAW") 

if __name__ == "__main__":
    main()