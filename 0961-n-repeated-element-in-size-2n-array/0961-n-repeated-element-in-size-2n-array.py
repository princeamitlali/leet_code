class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            if nums[i] in nums[i+1:]:
                return nums[i]
        