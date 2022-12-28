class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n %2 == 1:
            res.append(0)
            n -= 1
        print(n)
        for i in range(1,(n//2) + 1):
            res.append(i)
            res.insert(0,-1*i)
        return res
        