class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        lmax = [height[0]]
        n = len(height)
        for i in range(1,n):
            lmax.append(max(height[i],lmax[i-1]))
        # print(lmax)
        temp = height[::-1]
        rmax = [temp[0]]
        for i in range(1,n):
            rmax.append(max(temp[i],rmax[i-1]))
        rmax = rmax[::-1]
        # print(rmax)
        for i in range(n):
            res += min(rmax[i],lmax[i]) - height[i]
        return res