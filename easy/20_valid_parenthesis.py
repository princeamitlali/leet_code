"""
20. Valid Parentheses
Easy

13860

642

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
Accepted
2,375,097
Submissions
5,813,664


"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(', '}':'{',']':'['}
        l = -1
        for i in s:
            if l > -1:
                if i in dic and stack[l] == dic[i]:
                    stack.pop()
                    l -=1
                else:
                    stack.append(i)
                    l += 1
            else:
                stack.append(i)
                l += 1
        return True if len(stack) == 0 else False

"""
Runtime: 30 ms, faster than 95.06% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14 MB, less than 23.75% of Python3 online submissions for Valid Parentheses.

"""