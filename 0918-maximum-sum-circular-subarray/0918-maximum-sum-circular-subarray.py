class Solution:
    
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        if (n == 1):
            return nums[0]

        s = 0
        s = sum(nums)

        curr_max = nums[0]
        max_so_far = nums[0]
        curr_min = nums[0]
        min_so_far = nums[0]
        for i in range(1, n):
            curr_max = max(curr_max + nums[i], nums[i])
            max_so_far = max(max_so_far, curr_max)
            
            curr_min = min(curr_min + nums[i], nums[i])
            min_so_far = min(min_so_far, curr_min)
        
        if (min_so_far == s):
            return max_so_far
        return max(max_so_far, s - min_so_far)