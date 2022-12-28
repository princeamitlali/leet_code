class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()
        if target not in nums:
            return []
        # print((nums.index(target),nums[::-1].index(target)+1))
        for i in range(nums.index(target),len(nums) - nums[::-1].index(target)):
            res.append(i)
        return res
        