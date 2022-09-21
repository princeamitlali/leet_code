class Solution(object):
    def fourSum(self, nums, target):
        temp = []
        n = len(nums)
        nums.sort()
        for x in range(n-3):
            for i in range(x+1,n-2):
                low = i+ 1
                high = n-1
                while high> low:
                    su = nums[x] + nums[i] + nums[low] + nums[high]
                    if su == target:
                        temp.append((nums[x],nums[i] , nums[low] , nums[high]))
                    
                    if su > target:
                        high -= 1
                    else:
                        low +=1
        return set(temp)
        