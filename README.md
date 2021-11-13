# Tic Tac Toe Minimax

A Python implementation of Minimax AI Algorithm for the game Tic Tac Toe.

## How to Play

Run program to start playing. Choose preferred icon "X" or "O" and whether to start first or second. Choose whether AI runs minimax or randomly places move on board.

## Demonstration

This algorithm searches recursively for the best move to win or try to draw. It looks at the current board state and possible moves. For each possible moves it predicts where the other player would play until the game is over with either player winning or draw.

The clip below shows how the program works, with the AI winning the match. 

![](https://github.com/loheesong/tic_tac_toe_minimax/blob/master/README/ttt1.gif)

The clip below shows that AI will try to achieve a tie, which is the best outcome the second player can achieve given the first player plays optimally. 

![](https://github.com/loheesong/tic_tac_toe_minimax/blob/master/README/ttt2.gif)

### Random

This program also includes a random mode, where the AI will randomly place moves on the board until the game ends. The clip below showcases the random moves. 

![](https://github.com/loheesong/tic_tac_toe_minimax/blob/master/README/ttt4.gif)

## Limitations

Minimax assumes that the other player is playing optimally, or in this case, the human player is making moves to minimize the score. This can lead to interesting moves made by the AI as shown below.

In this situation, the optimal move would be to play 6 but instead 5 was played. 

![](https://github.com/loheesong/tic_tac_toe_minimax/blob/master/README/limitation1.JPG)

The AI decided that 2 was the better move so it was played. 6 was then played to try to block the AI but the AI still won due to having 2 opportunites to win. 

![](https://github.com/loheesong/tic_tac_toe_minimax/blob/master/README/limitation2.JPG)

## Technology

Python 3.9.1

## How to Use

Just download tictactoe.py and run, there is no need to install other packages as no additional packages were used. 
