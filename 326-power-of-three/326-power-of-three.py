class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        temp = 1
        while n > temp :
            temp *= 3
        return n == temp
        