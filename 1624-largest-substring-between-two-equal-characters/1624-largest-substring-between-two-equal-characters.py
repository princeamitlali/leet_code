class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = []
        r = -1
        n = len(s)
        for i in s:
            if i not in res:
                res.append(i)
                if s.count(i) > 1:
                    r = max(r,n-s[::-1].index(i) -2 - s.index(i)) 
            
        return r
        