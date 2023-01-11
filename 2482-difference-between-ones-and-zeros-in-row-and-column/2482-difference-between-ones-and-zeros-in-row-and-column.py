class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ones_row = []
        ones_col = []
        zero_row = []
        zero_col = []
        m,n = len(grid),len(grid[0])
        trans_grid = [list(i) for i in zip(*grid)]
        for row in grid:
            one = sum(row)
            zero = n - one

            ones_row.append(one)
            zero_row.append(zero)
        for row in trans_grid:
            one = sum(row)
            zero = m - one

            ones_col.append(one)
            zero_col.append(zero)


        result = [[0] * n for i in range(len(grid))]

        for r in range(m):
            for c in range(n):
                result[r][c] = ones_row[r] + ones_col[c] - zero_row[r] - zero_col[c]

        return result
        