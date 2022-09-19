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
            rmax.append(max(temp[i],rmax[i-1]))
        rmax = rmax[::-1]
        # for i in range(n):
        #     res += min(rmax[i],lmax[i])
        # return res
        print(rmax,lmax)
        temp = []
        for i in range(len(rmax)):
            temp.append(min(rmax[i],lmax[i]))
        print(temp)
        temp = sorted(temp)
        ma = 0
        n = len(temp)
        for i in range(n):
            val = temp[i] * (n-i-1)
            if val > ma:
                ma = val
        return ma
            
#         rmax = []
#         pre = height[0]
        
#         for i in height:
#             if i > pre:
#                 pre = i
#             rmax.append(pre)
#         print(rmax)
#         lmax = []
#         pre = height[-1]
#         for i in height[::-1]:
#             if i > pre:
#                 pre = i
#             lmax.append(pre)
#         print(lmax[::-1])
#         res = 0
#         # for i in range()
        
        
        