class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        i = 0
        while i < n-1:
            v = (nums[i] + 1) - nums[i+1]
            if v > 0:
                # v -= res
                res += v
                nums[i+1] = nums[i]+1
            print(v,res)
            i += 1
        return res
            
        