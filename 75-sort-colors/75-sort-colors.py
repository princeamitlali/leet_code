from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0,0,0]
        for i in nums:
            if i == 0:
                temp[0] = temp[0] + 1
            elif i == 1:
                temp[1] = temp[1] + 1
            else:
                temp[2] = temp[2] + 1
        print(temp)      
        i = 0
        j = 0
        n = len(nums)
        if i < n:
            
            while j < temp[0]:
                nums[i] = 0
                i += 1
                j += 1
            # print(nums)
        j = 0
        if i < n :
            while j < temp[1]:
                nums[i] = 1
                i += 1
                j += 1
            # print(nums)
        j = 0
        if i < n:
            
            while j < temp[2]:
                nums[i] = 2
                i += 1
                j += 1
            # print(nums)
        # i = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.insert(0,0)
        #     if nums[i] == 2:
        #         nums.pop(i)
        #         nums.append(2)
        #     print(nums)
        #     i += 1
        # while i < len(nums):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.insert(0,0)
        #     if nums[i] == 2:
        #         nums.pop(i)
        #         nums.append(2)
        #     print(nums)
        #     i += 1
                
        