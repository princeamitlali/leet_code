class Solution:
    def mySqrt(self, x: int) -> int:
        count = 0
        if x == 0:
            return 0
        while x > 0:
            x = x- 2*count + 1
            count += 1
        return count-2
        