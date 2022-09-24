class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = -984758959485 #seeding purpose
        for i in range(len(nums)):
            reach = max(reach, nums[i])
            if i == len(nums)-1:
                return True
            if reach == 0:
                return False
            reach = reach - 1
        
        return False
        