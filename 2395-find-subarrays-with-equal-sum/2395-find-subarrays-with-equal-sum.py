class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        res = []
        for i in range(len(nums)-1):
            su = nums[i]+ nums[i+1]
            if su in res:
                return True
            res.append(su)
        return False
        