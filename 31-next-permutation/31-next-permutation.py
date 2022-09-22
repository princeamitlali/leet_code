class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = -1
        ind =-1
        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i]>nums[i-1]:
                flag = i-1
                break
        if flag == -1:
            nums.reverse()
        else:
            for i in range(n-flag-1):
                val = nums[-i-1]
                if val > nums[flag]:
                    nums[flag],nums[-i-1] = nums[-i-1],nums[flag]
                    break
            left = flag + 1
            right = n-1
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1