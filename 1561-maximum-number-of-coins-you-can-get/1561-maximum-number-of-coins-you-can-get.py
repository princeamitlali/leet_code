class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        c = 0
        for i in range(len(piles)//3,len(piles),2):
            c += piles[i]
            
        return c
            
        