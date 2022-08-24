class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        temp = 1
        while n > temp :
            temp *= 3
        if n == temp:
            return True 
        return False
        