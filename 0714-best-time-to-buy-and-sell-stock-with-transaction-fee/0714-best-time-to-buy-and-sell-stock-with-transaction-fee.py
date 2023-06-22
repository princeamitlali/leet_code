class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # p = 0
        # prices.append(0)
        # s = prices[0]
        # for i in range(1,len(prices)-1):
        #     v = prices[i]-prices[i+1] -fee
        #     if v > 0:
        #         print(prices[i],s)
        #         p += prices[i] - s -fee
        #         s = prices[i+1]
        # if p < 0:
        #     return 0
        # return p
        ownShare, noShare = -prices[0], 0

        for price in prices:
            ownShare, noShare = (max(ownShare, noShare-price       ),
                                 max( noShare, ownShare + price-fee))

        return noShare
            
        