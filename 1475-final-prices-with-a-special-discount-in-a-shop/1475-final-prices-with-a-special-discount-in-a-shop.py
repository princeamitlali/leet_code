class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        if not prices:
            return None

        res = []
        for i in range(n-1):
            v = prices[i]
            for j in range(i+1,n):
                if prices[j] <= v:
                    v -= prices[j]
                    break
            res.append(v)
        res.append(prices[-1])
        return res
        