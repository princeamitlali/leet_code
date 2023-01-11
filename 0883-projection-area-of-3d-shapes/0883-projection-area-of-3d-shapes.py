class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid),(len(grid[0]))
        res = m *n
        trans = [list(i) for i in zip(*grid)]
        for i in grid:
            res -= i.count(0)
            res += max(i)
        for i in trans:
            res += max(i)
        # print(val)
        return res
        