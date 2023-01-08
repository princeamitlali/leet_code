from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        memo = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                ix, iy = points[i]
                jx, jy = points[j]
                a = math.inf if ix - jx == 0 else (iy - jy) / (ix - jx)
                b = ix if ix - jx == 0 else iy - a * ix

                memo[(a,b)].add(i)
                memo[(a,b)].add(j)
        
        ans = 0
        for key in memo.keys():
            ans = max(ans, len(memo[key]))

        return ans
        