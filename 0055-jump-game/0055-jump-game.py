class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = -1
        n = len(nums)
        for i in range(len(nums)):
            reach = max(reach, nums[i])
            if i == n-1:
                return True
            if reach == 0:
                return False
            reach = reach - 1
        
        return False
        