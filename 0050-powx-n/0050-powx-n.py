class Solution:
    def myPow(self, x: float, n: int) -> float:
        sol = 1.0
        nn = n
        if nn < 0:
            nn = -1 * nn

        while nn > 0:
            if nn %2:
                sol *= x
                nn -= 1
            else:
                x *= x
                nn = nn // 2

        if n < 0:
            return 1 / sol
        return sol
            
        