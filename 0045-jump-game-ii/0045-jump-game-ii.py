class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, curren_idx, furthest_idx = 0, 0, 0
        for i in range(len(nums) - 1):
            furthest_idx = max(furthest_idx, i + nums[i])
            if i == curren_idx:
                jumps += 1
                curren_idx = furthest_idx

        return jumps
        