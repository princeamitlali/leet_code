class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while (i*(i+1)/2)< n+1:
            i += 1
        return i-1
        