class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = 0
        f_sum = sum(nums)
        for i in range(len(nums)):
            # print(s,nums[i])
            if s == (f_sum -nums[i]-s):
                return i
            s += nums[i]
        if s == nums[-1]:
            return len(nums) - 1
        return -1
            
        