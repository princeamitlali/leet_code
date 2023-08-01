class Solution:
    def hcf(self,x,y):
        while(y):
            x, y = y, x % y
        return x
    def simplifiedFractions(self, n: int) -> List[str]:
        num = 1
        den = 1
        res = []
        while num <= n:
            for i in range(1,n+1):
                if self.hcf(num,i) == 1 and num /i <1:
                    res.append(str(num) + "/" + str(i))
                # print(num,i)
            num += 1
        return res
                
        