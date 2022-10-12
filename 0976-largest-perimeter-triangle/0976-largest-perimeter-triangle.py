class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        print(nums)
        for i in range(len(nums)-2):
            print(nums[i:i+3])
            if nums[i] < (nums[i+1] + nums[i+2]):
                return sum(nums[i:i+3])
        return 0
        