class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        r = len(s)
        bl = []
        for i in s[::-1]:
            if i == c:
                r = 0
            r += 1
            bl.append(r)
        bl = bl[::-1]
        fl = []
        r = len(s)
        for i in range(len(s)):
            if s[i] == c:
                r = 0
            r += 1
            fl.append(min(bl[i],r)-1)
        
        
        res = []
        for i in range(len(s)):
            res.append(min(fl[i],bl[i])-1)
        return fl
            
        