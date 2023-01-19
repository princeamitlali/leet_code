class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        r = len(s)
        fl = []
        for i in s:
            if i == c:
                r = 0
            r += 1
            fl.append(r)
        r = len(s)
        bl = []
        for i in s[::-1]:
            if i == c:
                r = 0
            r += 1
            bl.append(r)
        bl = bl[::-1]
        res = []
        for i in range(len(s)):
            res.append(min(fl[i],bl[i])-1)
        return res
            
        