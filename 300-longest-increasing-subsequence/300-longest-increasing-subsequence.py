class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums.pop(0)]         # use this list to track increasing
        
        for num in nums:            # add current number into the list
            if num > ans[-1]:
                ans.append(num)
            else:
                ans[bisect_left(ans, num)] = num
                
        return len(ans)
        
        