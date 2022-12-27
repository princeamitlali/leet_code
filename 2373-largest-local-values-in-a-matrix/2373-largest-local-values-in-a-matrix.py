class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        if n > 3:
            res = []
            for i in range(n-2):
                v = []
                for j in range(n-2):
                    v.append(max(max(grid[i][j:j+3]),max(grid[i+1][j:j+3]),max(grid[i+2][j:j+3])))
                    # v.append(max(max(grid[i:i+3][j:j+3]),max(grid[i+1:i+4][j:j+3]),max(grid[i+2:i+j][j:j+3])))
                res.append(v)
            return res
        return [[max(max(grid[0]),max(grid[1]),max(grid[2]))]]
        