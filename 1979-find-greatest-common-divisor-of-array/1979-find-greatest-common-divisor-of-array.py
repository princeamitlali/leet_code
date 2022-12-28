class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        l,s = nums[-1],nums[0]
        for i in range(s,0,-1):
            if l % i == 0 and s % i == 0:
                return i
        return 1
        