# import pygame

# create board
from typing import Tuple, Union


class Board:
    def __init__(self) -> None:
        self.row = 3
        self.col = 3
        self.BLANK = "."
        self.board = [[self.BLANK for _ in range(self.col)] for _ in range(self.row)]

    def _is_valid_move(self, location: Tuple[int, int]):
        """Checks for valid input"""
        row, col = location 
        print(row,col) 

        # if its in board
        if row < 0 or row > self.row - 1 or col < 0 or col > self.col - 1:
            return False 

        # if it replaces other players move
        if self.board[row][col] != self.BLANK:
            return False 
        
        return True

    def move(self, player: str, location: Tuple[int, int]) -> bool:
        """Accept player input and places move, returns True if successful else False"""
        if not self._is_valid_move(location):
            return False
            
        row, col = location
        print(row,col) 
        self.board[row][col] = player
        return True
    
    def game_won(self, player) -> bool:
        """Logic to check win condition"""
        # horizontal
        for i in self.board:
            pass
        # vertical
        # diagonal

        pass 

    def print_board(self):
        """Pretty print board"""
        for i in self.board:
            print(i)

def sanitize_input(raw_input: str) -> Union[bool, Tuple[int, int]]:
    """Returns locations in tuple if pass tests else False"""
    # no blank string
    if not raw_input:
        return False

    # only digits
    clean = []
    # make sure input can be turned to int
    for i in raw_input.split():
        try:
            clean.append(int(i))
        except ValueError:
            return False

    # make sure its only coordinates row and col
    if len(clean) != 2:
        return False
    
    return clean[0], clean[1]

def main():
    """Main game logic here"""
    board = Board()
    turn = 0
    while True:
        raw_input = input("Location: ")
        print(sanitize_input(raw_input))
    # while turn < 3:
    #     raw_input = input("Location: ")
        
    #     board.print_board()
    #     turn += 1

if __name__ == "__main__":
    main()