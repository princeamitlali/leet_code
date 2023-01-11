class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
#         m = len(grid)
#         n = len(grid[0])
#         trans_grid = [list(i) for i in zip(*grid)]
        
#         res=[[0] * n for i in range(m)]
#         # print(trans_grid)
#         for i in range(m):
#             for j in range(n):
#                 # print(grid[i], trans_grid[i] )
#                 res[i][j] = grid[i].count(1) + trans_grid[j].count(1) - grid[i].count(0)- trans_grid[j].count(0)
#             # print(res)
#         return res

        ones_row = []
        ones_col = []
        zero_row = []
        zero_col = []
        trans_grid = [list(i) for i in zip(*grid)]
        for row in grid:
            one = sum(row)
            zero = len(grid[0]) - one

            ones_row.append(one)
            zero_row.append(zero)
        for row in trans_grid:
            one = sum(row)
            zero = len(trans_grid[0]) - one

            ones_col.append(one)
            zero_col.append(zero)


        result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                result[r][c] = ones_row[r] + ones_col[c] - zero_row[r] - zero_col[c]

        return result
        