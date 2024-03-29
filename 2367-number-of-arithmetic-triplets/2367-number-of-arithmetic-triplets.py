class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # n = len(nums)
        # c = 0
        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         for k in range(j+1,n):
        #             if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
        #                 c += 1
        # return c
        triplets = 0
        for elem in range(len(nums)-1, -1, -1):
            if (nums[elem] - diff) in nums and (nums[elem] - (diff*2)) in nums:
                triplets += 1
        return triplets
        