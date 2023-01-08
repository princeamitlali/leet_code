class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid) - 1
        n = len(grid[0]) - 1

        def dfs(x, y):
            grid[x][y] = -1
            g = d = h = b = 0
            if x + 1 <= m and grid[x + 1][y] == 1:
                d = dfs(x + 1, y)
            if y + 1 <= n and grid[x][y + 1] == 1:
                b = dfs(x, y + 1)
            if x - 1 >= 0 and grid[x - 1][y] == 1:
                g = dfs(x - 1, y)
            if y - 1 >= 0 and grid[x][y - 1] == 1:
                h = dfs(x, y - 1)
            return 1 + g + d + b + h

        for i in range(m + 1):
            for j in range(n + 1):
                if grid[i][j] != -1: # not visited
                    if grid[i][j] == 1:
                        res = max(dfs(i, j), res)
                    else:
                        grid[i][j] = -1
        return res
        