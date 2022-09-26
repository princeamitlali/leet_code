class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for i in range(9):
            for c in range(9):
                if board[i][c] == ".":
                    continue
                if (
                    board[i][c] in rows[i]
                    or board[i][c] in cols[c]
                    or board[i][c] in squares[(i // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[i][c])
                rows[i].add(board[i][c])
                squares[(i // 3, c // 3)].add(board[i][c])

        return True
    
#         for i in board:
#             val = [0] * 9
#             for j in i :
#                 if j!= ".":
#                     ind = int(j) -1
#                     if val[ind] == 1:
#                         return False
#                     else:
#                         val[ind] = 0
#         for i in range(9):
#             val = [0] * 9
#             for j in range(9) :
#                 if board[j][i]!= ".":
#                     ind = int(j)-1
#                     if val[ind] == 1:
#                         return False
#                     else:
#                         val[ind] = 0
                        
                        
#         import numpy as np
#         array1 = np.array(board)
#         n = [np.split(array1,[3,6])]
#         temp = []
#         for i in n:
#             x,y = 0,0
#             for a in range()
#         print(temp)
#         return True
                    
                        
                    
        