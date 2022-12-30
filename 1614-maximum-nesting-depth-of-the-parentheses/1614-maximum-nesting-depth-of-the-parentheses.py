class Solution:
    def maxDepth(self, s: str) -> int:
        res = ""
        for i in s:
            if i == "(" or i == ")":
                res += i
        print(res)
        while ")(" in res:
            res = res.replace(")(","")
        return len(res) //2
        