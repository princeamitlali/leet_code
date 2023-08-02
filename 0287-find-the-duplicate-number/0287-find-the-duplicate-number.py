class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while True:
            # print(nums)
            if nums[i] == 0:
                return i
            j = nums[i]
            nums[i] = 0
            i = j
            


        