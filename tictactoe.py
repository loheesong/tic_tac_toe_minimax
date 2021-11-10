# import pygame

import math
from typing import List, Tuple, Union

class Board:
    def __init__(self) -> None:
        self.row = 3
        self.col = 3
        self.BLANK = "."
        self.board = [[self.BLANK for _ in range(self.col)] for _ in range(self.row)]

    def _is_valid_move(self, location: Tuple[int, int]):
        """
        A move is valid if the chosen cell is empty

        :param location: X coordinate
        :return: True if the board[x][y] is empty
        """
        return True if location in self._empty_square() else False

    def _empty_square(self) -> List[Tuple[int, int]]:
        """
        Each empty square will be added into location list

        :return: a list of locations (tuple)
        """
        locations = []

        for x, row in enumerate(self.board):
            for y, square in enumerate(row):
                if square == self.BLANK:
                    locations.append((x, y))

        return locations

    def is_win(self, player: str):
        """
        Checks horizontal, vertical, diagonal if player wins

        :param player: -- a human or a computer
        :return: True if the player wins
        """
        win_state = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],

            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],

            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]
        return True if [player, player, player] in win_state else False

    def move(self, player: str, location: Tuple[int, int]) -> bool:
        """
        Place move on board, if the location is valid

        :param player: the current player
        :param location: location of move
        :return: True if move is successfully placed
        """
        row, col = location
        if self._is_valid_move(location):
            self.board[row][col] = player
            return True
        else:
            return False

    def minimax(self, depth: int, maximizingPlayer):
        """
        Minimax algorithm

        :param depth: node index in the tree (0 <= depth <= 9)
        :param player: an human or a computer
        :return: a list with [the best row, best col, best score]
        """
        """if depth == 0 or game over in position
            return static evaluation of position
    
        if maximizingPlayer:
            maxEval = -math.inf
            for each child of position
                eval = minimax(child, depth - 1, False)
                maxEval = max(maxEval, eval)
            return maxEval
        else:
            minEval = math.inf
            for each child of position
                eval = minimax(child, depth - 1, true)
                minEval = min(minEval, eval)
            return minEval"""
        pass 

    def print_board(self):
        """
        Pretty print board
        """
        for i in self.board:
            print(i)

def main():
    """Main game logic here"""
    board = Board()
    turn = 0
    while True:
        player_input = tuple(int(i) for i in input(f"Location: ").split())
        print(f"Location: {player_input} Turn: {turn}")
        # player 1
        if turn % 2 == 0:
            board.move("X", player_input) 
        # player 2 
        else:
            board.move("O", player_input) 

        board.print_board()
        if board.is_win("X"):
            print("X won")
            break
        elif board.is_win("O"):
            print("O won")
            break
        turn += 1

if __name__ == "__main__":
    main()