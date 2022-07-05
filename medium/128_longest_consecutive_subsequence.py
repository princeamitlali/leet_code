"""
128. Longest Consecutive Sequence
Medium

10458

463

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
Accepted
736,658
Submissions
1,508,965

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)), reverse= True)
        count = 0 
        maxi = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i] - nums[i+1] == 1:
                count += 1   
            else:
                if count > maxi:
                    maxi = count
                count = 0
        if count > maxi:
            maxi = count
        return maxi+1
    
"""
Success
Details 
Runtime: 285 ms, faster than 97.22% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 28.5 MB, less than 42.76% of Python3 online submissions for Longest Consecutive Sequence.

"""