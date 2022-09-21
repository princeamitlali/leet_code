class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp = x
        flag = True
        if abs(x) == 1:
            if n % 2 == 0:
                return 1
            return x
        flag = False
        if n == 0:
            return 1
        if n < 0 :
            n = -n
            flag = True
        p = 1
        while p+p < n:
            temp *= temp
            p += p
            if abs(temp) < 0.00001:
                return 0
            if flag and (abs(1/temp) < 0.000001):
                return 0
        while p < n:
            temp *= x
            p += 1
            if abs(temp) < 0.000001:
                return 0
            if flag and (abs(1/temp) < 0.000001):
                return 0
        print(temp)
        return 1/temp if flag else temp