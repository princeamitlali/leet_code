class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        m = 0
        for i in gain:
            res += i
            m = max(m,res)
        return m
        