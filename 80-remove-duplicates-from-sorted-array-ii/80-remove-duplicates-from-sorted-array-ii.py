class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        n = len(nums)
        while i < n -2:
            if nums[i] == nums[i+1] and nums[i] == nums[i+2]:
                nums.pop(i)
                i -= 1
                n-= 1
            i += 1
        return len(nums)
        