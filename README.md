# ChessNeuralNetwork #

A Neural Network that calculates every possible move by a player in a chess game, as well as every possible move made by the opponent. This is not limited to one move but rather every move in a game by both parties. 

> **Board:**
> A multi-dimensional char array of 8x8 will represent the chess board, K-king, Q-queen, B-bishop, R-rook, N-knight, P-pawn.
> 
> **Game:**
> The Neural Network is created in a tree structure with each node representing a position on a chess board. The head will be the begining of the game, the number of children is the number of possible moves in node's possition. 
