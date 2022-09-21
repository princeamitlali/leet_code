class Solution(object):
    def longestValidParentheses(self, s):
        n = len(s)
        flag = [False] * n
        stack = []
        print(flag)
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    flag[i] = True
                    flag[stack.pop()] = True
        print(flag)
        res = 0
        count = 0
        for i in flag:
            if not i:
                res = max(res,count)
                count = -1
            count += 1
            print(res,count)
        return max(res,count)
        
        