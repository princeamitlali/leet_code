class Solution:
    def diagonalSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        start,end = 0,n-1
        for i in grid:
            
            if start < end:
                
                res += i[start] + i[end]
            else:
                s ,e = end,start
                
                res += i[s] + i[e]
            if start == end:
                res -= i[start]
            start += 1
            end -= 1
            
        return res
        