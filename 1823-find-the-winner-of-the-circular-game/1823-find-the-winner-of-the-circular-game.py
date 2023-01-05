class Solution:
    def findTheWinner(self, n: int, m: int) -> int:
        def surviver(n,m):
            if n == 1:
                return 0
            return (surviver(n-1,m) + m ) % n
        return 1+ surviver(n,m)
        