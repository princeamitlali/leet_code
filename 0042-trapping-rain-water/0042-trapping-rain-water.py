class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        lmax = [height[0] ] * n
        rmax = [height[-1] ] * n
        # lma
        for i in range(1,n):
            lmax[i] = max(height[i],lmax[i-1])
            rmax[n-i-1] = max(height[n-i-1],rmax[n-i])
        # print(rmax)
        # print(lmax)
        # temp = height[::-1]
        # rmax_new = [temp[0]]
        # for i in range(1,n):
        #     rmax_new.append(max(temp[i],rmax_new[i-1]))
        # rmax_new = rmax_new[::-1]
        # print(rmax_new)
        for i in range(n):
            res += min(rmax[i],lmax[i]) - height[i]
        return res