from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # res = []
        # :
        #     res.append(list(i))
        return [list(i) for i in list(combinations([i+1 for i in range(n)],k))]
        