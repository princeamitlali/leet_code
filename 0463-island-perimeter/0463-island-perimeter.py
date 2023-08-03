class Solution:
    def islandPerimeter(self, grid: List[List[int]]):
        m = len(grid)
        n = len(grid[0])
        def isValid(i,j):
            # print(i,j)
            if i < 0 or i >m-1:
                return True
            if j < 0 or j > n-1:
                return True
            if grid[i][j] == 0:
                return True
            return False
        c = 0  
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if isValid(i-1,j):
                        c += 1
                    if isValid(i+1,j):
                        c += 1
                    if isValid(i,j+1):
                        c += 1
                    if isValid(i,j-1):
                        c += 1
        
                   
        return c
                    
        
        
        