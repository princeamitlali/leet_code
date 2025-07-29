class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums[1:]) == 0:
            return 0
        
        for i in range(1,len(nums)):
            sum1 = sum(nums[:i-1])
            sum2 = sum(nums[i:])
            print(sum1,sum2,i)
            if sum1 == sum2:
                return i - 1
        if sum(nums[:-1]) == 0:
            return len(nums) -1
        return -1
        