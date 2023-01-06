from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        v = combinations([i+1 for i in range(n)],k)
        res = []
        for i in list(v):
            res.append(list(i))
        return res
        