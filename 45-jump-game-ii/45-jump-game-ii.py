class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, curren_idx, furthest_idx = 0, 0, 0
        for i in range(len(nums) - 1):
            furthest_idx = max(furthest_idx, i + nums[i])
            if i == curren_idx:
                jumps += 1
                curren_idx = furthest_idx
        return jumps
        # if len(nums) == 1:
        #     return 0
        # def traverse(li):
        #     if len(li) <= 1:
        #         return 0
        #     if li[0] == len(li):
        #         return 1
        #     if li[0] > len(li):
        #         return 1
        #     res = 99999
        #     for i in range(li[0]):
        #         res = min(res,traverse(li[i+1:]))
        #         # print(res,i)
        #     return 1 + res
        # return traverse(nums)
        