class Solution:
    def kadane(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(max(nums), 0)
    
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        sums = sum(arr)
        mod = 10**9 + 7
        if k == 1:
            return self.kadane(arr) % (mod)
        if sums > 0:
            return (self.kadane(arr+arr) + (k-2)*sums) % (mod)
        else:
            return self.kadane(arr+arr) % (mod)