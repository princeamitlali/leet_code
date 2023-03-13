class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        v = 1
        for i in nums:
            v *= (i+0.000000000000000000000009)
          
        for i in range(len(nums)):
            nums[i] = int(v / (nums[i]+0.000000000000000000000009))
        return nums
        
        