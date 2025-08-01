class Solution:
    def maxDepth(self, s: str) -> int:
        sol = 0
        count = 0
        for i in s:
            if i == "(":
                count += 1
            if i == ")":
                sol = max(sol,count)
                count -= 1

        return max(sol,count)