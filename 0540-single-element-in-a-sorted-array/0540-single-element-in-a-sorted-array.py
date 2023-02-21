class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        v = nums[0]
        for i in nums[1:]:
            v ^= i
        return v
        