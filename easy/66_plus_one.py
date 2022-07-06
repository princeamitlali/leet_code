"""
66. Plus One
Easy

4555

4266

Add to List

Share
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
Accepted
1,259,095
Submissions
2,922,881
Seen this question in a real interview before?

Yes

No

"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = str(int("".join(map(str,digits))) + 1 )
        digits = []
        for i in val:
            digits.append(int(i))

        return digits
        
        
"""
Success
Details 
Runtime: 43 ms, faster than 67.92% of Python3 online submissions for Plus One.
Memory Usage: 13.9 MB, less than 11.01% of Python3 online submissions for Plus One.

"""