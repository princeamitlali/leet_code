class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        if len(rectangles) == 1:
            return 1
        res = []
        for i in rectangles:
            res.append(min(i))
        res.sort(reverse = True)
        c = 0
        init = res[0]
        for i in res:
            if i != init:
                return c
            c += 1
        return res
        