class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[-1]*101 for i in range(101)]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def count(i, j):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            if i == m - 1 and j == n - 1:
                if obstacleGrid[i][j]==1:
                    return 0
                dp[i][j] = 1
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = count(i+1,j) + count(i,j+1)
            return dp[i][j]
        return count(0,0)