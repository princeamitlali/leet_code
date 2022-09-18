class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        elif n < 3:
            return True
        else:
            while True:
                if n % 5 == 0:
                    n = n//5
                elif n % 3 == 0:
                    n = n//3
                elif n % 2 == 0:
                    n = n //2
                else:
                    break
        if n == 1:
            return True
        return False