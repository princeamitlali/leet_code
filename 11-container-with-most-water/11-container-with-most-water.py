class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        lmax = [height[0]]
        n = len(height)
        for i in range(1,n):
            lmax.append(max(height[i],lmax[i-1]))
        temp = height[::-1]
        rmax = [temp[0]]
        for i in range(1,n):
            rmax.append(min(max(temp[i],rmax[i-1]),lmax[n-i-1]))
        rmax = sorted(rmax[::-1])
        ma = 0
        n = len(rmax)
        for i in range(n):
            val = rmax[i] * (n-i-1)
            if val > ma:
                ma = val
        return ma
        
        
        