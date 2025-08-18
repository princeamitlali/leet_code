class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        maxLen = 0
        zeros = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            maxLen = max(maxLen, r-l + 1)
            r += 1
        return maxLen

        