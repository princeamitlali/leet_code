class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[-1 for _ in range(i + 1)] for i in range(len(triangle) + 1)]
        # print(dp)
        def dfs(i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            left = triangle[i][j] + dfs(i + 1, j)
            right = triangle[i][j] + dfs(i + 1, j + 1)
            dp[i][j] = min(left, right)
            return dp[i][j]
        return dfs(0, 0)
        