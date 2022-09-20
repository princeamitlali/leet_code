class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                elif nums[i] + nums[l] + nums[r]>0:
                    r-=1
                else:
                    l+=1
        return set(res)
#         temp = []
#         n = len(nums)
#         nums = sorted(nums)
#         for i in range(n):
#             low = i+ 1
#             high = n-1
#             while high> low:
                
#                 t = [nums[i] , nums[low] , nums[high]]
#                 su = sum(t)
#                 # print(t)
#                 if su == 0:
#                     if t not in temp:
#                         temp.append(t)
#                     # low += 1
#                     # high -= 1
#                 if su > 0:
#                     high -= 1
#                 else:
#                     low +=1
#         return temp
                
        