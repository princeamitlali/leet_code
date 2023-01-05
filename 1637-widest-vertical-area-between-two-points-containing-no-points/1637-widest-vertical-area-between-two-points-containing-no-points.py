class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        res = []
        for i in points:
            res.append(i[0])
        res.sort()
        r = 0
        for i in range(len(res)-1):
            r = max(r,res[i+1]-res[i])
        return r