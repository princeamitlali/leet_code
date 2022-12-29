from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = Counter
        v = c(stones)
        c = 0
        for i in jewels:
            if i in v.keys():
                c += v[i]
        return c
            
        