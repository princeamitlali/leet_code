class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # res=[]
        # for i in range(len(nums)):
        #     l = i+1
        #     r = len(nums)-1
        #     while l<r:
        #         if nums[i] + nums[l] + nums[r] == 0:
        #             res.append((nums[i], nums[l], nums[r]))
        #             l+=1
        #             r-=1
        #         elif nums[i] + nums[l] + nums[r]>0:
        #             r-=1
        #         else:
        #             l+=1
        # return set(res)
        temp = []
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            low = i+ 1
            high = n-1
            while high> low:
                su = nums[i] + nums[low] + nums[high]
                if su == 0:
                    temp.append((nums[i] , nums[low] , nums[high]))
                    # low += 1
                    # high -= 1
                if su > 0:
                    high -= 1
                else:
                    low +=1
        return set(temp)
                
        