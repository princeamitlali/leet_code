from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter
        val = c(nums)
        res = 0
        for i in val:
            if val[i] == 1:
                res += i
        return res
        