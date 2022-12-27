class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        count = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                count += 1
                i += 1
            i += 1
        return [count, len(nums)- 2 * count]