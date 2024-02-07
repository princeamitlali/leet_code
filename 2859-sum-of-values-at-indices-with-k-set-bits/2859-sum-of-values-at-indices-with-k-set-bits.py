class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        for v in range(len(nums)):
            if sum([int(i) for i in bin(v)[2:]]) == k:
                res += nums[v]
        return res
     