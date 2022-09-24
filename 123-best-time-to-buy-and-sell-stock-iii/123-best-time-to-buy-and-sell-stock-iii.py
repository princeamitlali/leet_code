class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        left_max=[0 for x in range(0,n)]
        right_max=[0 for x in range(0,n)]
        temp_min=prices[0]
        for i in range(1,n):
            left_max[i]=max(left_max[i-1],prices[i]-temp_min)
            temp_min=min(temp_min,prices[i])
        temp_max=prices[n-1]
        for i in range(n-2,-1,-1):
            right_max[i]=max(right_max[i+1],(temp_max-prices[i]))
            temp_max=max(temp_max,prices[i])
        ans=right_max[0]
        for i in range(1,n):
            ans=max(ans,left_max[i-1]+right_max[i])
        return ans