class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)-2):
            st = s[i:i+3]
            # print(st)
            if len(set(st))== 3:
                res += 1
        
        return res
        