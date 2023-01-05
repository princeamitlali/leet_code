class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        v = sorted(piles)
        res = 0
        while len(v) >0:
            v.pop()
            res += v[-1]
            v.pop()
            v.pop(0)
            # print(v,piles)
            
        return res
            
        