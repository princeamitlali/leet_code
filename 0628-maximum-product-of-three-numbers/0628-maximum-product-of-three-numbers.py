class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        v = 0
        if nums[0] < 0 and nums[1]<0:
            v = nums[0] * nums[1]
        val = [nums[-1] *v,v*nums[-2], v  * nums[-3],nums[-1] * nums[-2] * nums[-3]]
        return max(val)
        