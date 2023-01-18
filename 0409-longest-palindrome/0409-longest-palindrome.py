
class Solution:
    def longestPalindrome(self, nums: str) -> int:
        flag = 0
        res= 0
        if len(set(nums)) == 1:
            return len(nums)
        for i in set(nums):
            c = nums.count(i)
            if c % 2 == 0:
                res += c
            else:
                res += c-1
                flag = 1
        return res + flag      