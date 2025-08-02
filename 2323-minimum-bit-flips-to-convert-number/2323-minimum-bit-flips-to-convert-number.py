class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        sol = start ^ goal
        res = 0
        while sol > 0:
            res += sol % 2
            sol = sol //2
        
        return res