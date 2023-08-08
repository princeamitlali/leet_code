class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mi,mx = min(nums),max(nums)
        c = -1
        for i in nums:
            if mi < i <mx:
                return i
        
        return c
        