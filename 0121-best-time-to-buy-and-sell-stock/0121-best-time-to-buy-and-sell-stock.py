class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float("inf")
        best_profit =  0
        for price in prices:
            profit = price - lowest_price
            
            if profit > best_profit :
                best_profit = profit
            if price < lowest_price:
                lowest_price = price
        return best_profit            