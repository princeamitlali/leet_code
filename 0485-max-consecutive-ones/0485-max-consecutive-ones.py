class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ma = 0
        for i in nums:
            if i == 0:
                ma = max(ma,count)
                count = -1
            count += 1
            print(ma,count)
        return max(ma,count)
        