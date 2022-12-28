class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDivide(n):
            if "0" in str(n):
                return False
            for i in str(n):
                if n % int(i) != 0:
                    return False
            return True
        res = []
        for i in range(left,right+1):
            
            if isSelfDivide(i):
                res.append(i)
        return res
        