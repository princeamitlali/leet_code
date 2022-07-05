"""
14. Longest Common Prefix
Easy

8798

3148

Add to List

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
Accepted
1,683,523
Submissions
4,220,233

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key = lambda x : len(x))
        val = strs[0]
        pos = 0
        flag = False

        for i in val:
            for j in strs:
                if i != j[pos]:
                    flag = True
                    break
            if flag:
                break
            pos += 1

        return val[:pos]


"""
Success
Details 
Runtime: 54 ms, faster than 48.08% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 49.69% of Python3 online submissions for Longest Common Prefix.

"""