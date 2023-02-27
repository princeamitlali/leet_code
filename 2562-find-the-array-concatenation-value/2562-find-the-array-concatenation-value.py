class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i = 0 
        res = 0
        j = len(nums)-1
        while j > i:
            v = str(nums[i]) + str(nums[j])
            res += int(v)
            i +=1
            j -= 1
        if i == j:
            res += nums[i]
        return res