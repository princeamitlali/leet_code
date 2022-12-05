class Solution:
    def su(self,v):
        t = 0
        while v > 0:
            t += v %10
            v = v // 10
        return t
    def getLucky(self, s: str, k: int) -> int:
        t=""
        for i in range(len(s)):
            t += str(ord(s[i])-96)
        res = int(t)
        while k > 0:
            res = self.su(res)
            k -= 1
        return res
        
    
        