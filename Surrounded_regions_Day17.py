Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Python3 program:

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        height  = len(board)
        width = len(board[0])
        
        def mark(r,c):
            if 0<=r<height and 0<=c<width and board[r][c] =='O':
                board[r][c] = 'C'
                mark(r-1,c)
                mark(r+1,c)
                mark(r,c-1)
                mark(r,c+1)
                
        #first row/last row
        for r in [0,height-1]:
            for c in range(width):
                mark(r,c)
        #first column/last column
        for c in [0,width-1]:
            for r in range(height):
                mark(r,c)
                
        for r in range(height):
            for c in range(width):
                if board[r][c] == 'C':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
     
