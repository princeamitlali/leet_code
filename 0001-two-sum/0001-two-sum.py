class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if dic.get(n,None) == None:
                dic[nums[i]] = i
            else:
                return [i,dic.get(n)]
        