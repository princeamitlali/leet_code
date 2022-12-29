class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if nums[abs(x)-1] > 0:
                nums[abs(x)-1]*=-1
        # print(nums)
        for i, x in enumerate(nums):
            if x> 0:
                res.append(i+1)
            # else:
                
        return res
        