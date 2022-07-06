"""
509. Fibonacci Number
Easy

4077

274

Add to List

Share
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:

0 <= n <= 30
Accepted
866,955
Submissions
1,262,467
Seen this question in a real interview before?

Yes

No

"""

class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return n
        first,second = 0,1
        for _ in range(1,n):
            first,second = second,first+second
        return second
        
        
"""
Success
Details 
Runtime: 35 ms, faster than 86.37% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.8 MB, less than 95.78% of Python3 online submissions for Fibonacci Number.

"""
