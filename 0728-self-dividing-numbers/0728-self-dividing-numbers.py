class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDivide(n):
            for i in str(n):
                if n % int(i) != 0:
                    return False
            return True
        res = []
        for i in range(left,right+1):
            
            if "0" not in str(i) and isSelfDivide(i):
                res.append(i)
        return res
        