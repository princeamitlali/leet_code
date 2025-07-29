class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
            exit()
        min_a = min(j[0] for j in ops)
        min_b = min(j[1] for j in ops)
        return min_a * min_b