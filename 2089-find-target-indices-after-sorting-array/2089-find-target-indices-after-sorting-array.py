class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        if target not in nums:
            return []
        res = []
        nums.sort()
        for i in range(nums.index(target),len(nums) - nums[::-1].index(target)):
            res.append(i)
        return res
        