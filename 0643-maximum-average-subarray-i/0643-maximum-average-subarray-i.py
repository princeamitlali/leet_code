class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)
        m = sum(nums[:k])
        v = m
        for i in range(k,len(nums)):
            v = (v+ nums[i] - nums[i-k])
            m = max(m,v)
        return m / k
        