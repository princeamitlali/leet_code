class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i = 0 
        res = 0
        j = len(nums)-1
        while j > i:
            res += int(str(nums[i]) + str(nums[j]))
            i +=1
            j -= 1
        if i == j:
            res += nums[i]
        return res