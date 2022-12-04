class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = 0
        n = len(nums)
        for i in range(n-1):
            s2 += nums[i]
            nums[i] = abs(s2//(i+1) - (s1-s2)// (n-i-1))
        nums[-1] = s1//n
        return nums.index(min(nums))
            
        