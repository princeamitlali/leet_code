class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m  = len(matrix)
        n = len(matrix[0])
        row = [False] * m
        col = [False] * n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
                    
        for i in range(m):
            for j in range(n):
                if col[j] or row[i]:
                     matrix[i][j] = 0
                
        