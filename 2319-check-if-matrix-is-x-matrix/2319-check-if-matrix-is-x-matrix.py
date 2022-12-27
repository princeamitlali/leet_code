class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)
        start,end = 0,n-1
        for i in grid:
            if start < end:
                if i[start] == 0 or i[end] == 0:
                    return False
                if sum(i[:start]) >0  or sum(i[start+1:end]) > 0 or sum(i[end+1:])> 0:
                    return False
            else:
                s ,e = end,start
                if i[s] == 0 or i[e] == 0:
                    return False
                if sum(i[:s]) >0  or sum(i[s+1:e]) > 0 or sum(i[e+1:])> 0:
                    return False
            start += 1
            end -= 1
        return True
             
            
        