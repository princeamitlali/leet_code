class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum,rightsum = 0, sum(nums)
        for i in range(len(nums)):
            rightsum -= nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1
        