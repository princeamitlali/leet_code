class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = sorted(nums)
        for i in range(len(nums)):
            nums[i] = n.index(nums[i])
        return nums
        