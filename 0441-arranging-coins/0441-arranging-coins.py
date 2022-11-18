class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 3:
            return 1
        i = 0
        while True:
            i += 1
            val = i * (i + 1)
            val = val /2
            if val > n:
                return i -1
            if val == n:
                return i
        