class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        i = 1
        for num in nums:
            if num == i:
                i += 1
            else:
                if num> 0:
                    return i
        return i
#         mi = min(nums)
#         mx = max(nums)
#         if mx < 1:
#             return 1
#         if mx == 1:
#             return 2
#         if mi > 1:
#             return 1
            
#         for i in range(mi,mx):
#             if i not in nums:
#                 return i
#         if mi > 1:
#             return 1
#         else:
#             return mx + 1
        # mi = pow(2,31)
        # mx = 0
        # su = 0
        # for i in nums:
        #     if i > 0:
        #         mi = min(mi,i)
        #         mx = max(mx,i)
        #         su += i
        # val = ((mx*(mx+1) /2)- (mi*(mi+-1) /2)) -su
        # if mx < 1:
        #     return 1
        # if mx == 1:
        #     return 2
        # print(val)
        # if mi > 1:
        #     return 1
        # if val < 1:
        #     return mx + 1
        # return val
        
            