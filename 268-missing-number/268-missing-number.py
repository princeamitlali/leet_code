class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        su = len(nums)*(len(nums)+1)/2
        for i in nums:
            su -= i
        return int(su)
        
            
        