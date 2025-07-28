class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        lmax = [height[0] ] * n
        rmax = [height[-1] ] * n
        for i in range(1,n):
            lmax[i] = max(height[i],lmax[i-1])
            rmax[n-i-1] = max(height[n-i-1],rmax[n-i])
 
        for i in range(n):
            res += min(rmax[i],lmax[i]) - height[i]
        return res