"""
28. Implement strStr()
Easy

4424

3764

Add to List

Share
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
Accepted
1,309,886
Submissions
3,590,630
Seen this question in a real interview before?

Yes

No

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1
    
"""
Success
Details 
Runtime: 36 ms, faster than 80.76% of Python3 online submissions for Implement strStr().
Memory Usage: 13.8 MB, less than 63.36% of Python3 online submissions for Implement strStr().

"""