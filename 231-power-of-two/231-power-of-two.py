import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        val = math.log2(n)
        return val == val//1