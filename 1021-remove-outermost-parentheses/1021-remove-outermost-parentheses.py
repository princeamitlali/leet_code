class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        o,c = 0,0
        res = []
        r = ""
        for i in s:
            if i=="(":
                o += 1
            if i == ")":
                o-= 1
            r += i
            if o == 0:
                res.append(r)
                r = ""
        for i in res:
            r += i[1:-1]
        return r
        