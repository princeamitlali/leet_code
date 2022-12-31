from collections import Counter
class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter
        v = c(num)
        print(v)
        
        for i in range(len(num)):
            print(i,v[str(i)],num[i])
            if v[str(i)] != int(num[i]):
                return False
                    
        return True
        