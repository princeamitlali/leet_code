class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        sum_arr = []
        for i in range(len(nums)):
            sum_arr.append(abs(sum(nums[:i])-sum(nums[i+1:])))
        return sum_arr
        