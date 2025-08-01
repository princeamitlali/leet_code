class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        outer = 0
        start = 0
        res = []
        for i in range(len(s)):
            if s[i]=="(":
                outer += 1
            if s[i] == ")":
                outer -= 1
            if outer == 0:
                res.append(s[start+1:i])
                start = i+1
        # print(res)
        return "".join(i for i in res)
        