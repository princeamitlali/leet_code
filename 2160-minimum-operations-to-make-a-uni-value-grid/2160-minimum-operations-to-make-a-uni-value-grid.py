class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        li= []
        for i in grid:
            for j in i:
                li.append(j)
        if len(li) < 2:
            return 0
        li.sort()
        res = 0
        cen = li[len(li)//2]
        for i in li:
            v = abs(cen - i)
            if v % x != 0:
                return -1
            res += v //x
        return res
        