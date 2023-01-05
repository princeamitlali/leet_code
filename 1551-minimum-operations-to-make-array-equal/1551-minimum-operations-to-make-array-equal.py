class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            n = n/2
            return int(n * n)
        else:
            n = n //2
            return int(n*(n+1))
        