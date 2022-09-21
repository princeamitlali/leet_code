class Solution(object):
    def longestValidParentheses(self, s):
        n = len(s)
        flag = [True] * n
        stack = []
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    flag[i] = False
                    flag[stack.pop()] = False
        res = 0
        count = 0
        for i in flag:
            if i:
                res = max(res,count)
                count = -1
            count += 1
        return max(res,count)
        
        