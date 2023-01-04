class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        res1 = []
        for i in grid:
            res1.append(max(i))
        print(res1)
        # tm = zip(*a)
        res2 = []
        for i in zip(*grid):
            res2.append(max(i))
        print(res2)
        res = 0
        for i in range(len(res1)):
            for j in range(len(res2)):
                v = min(res1[i],res2[j])
                v -= grid[i][j]
                if v >0:
                    res += v
        
        
        return res
        