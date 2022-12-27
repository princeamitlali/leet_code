class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res = []
        for i in s:
            if i in res:
                return i
            res.append(i)
        