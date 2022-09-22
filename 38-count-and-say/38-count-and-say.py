from collections import Counter
class Solution:
    def countAndSay(self, n: int) -> str:
        temp = 11
        if n == 1:
            return "1"
        while n > 2:
            count = 1
            val = str(temp) + "."
            temp = 0
            for i in range(1,len(val)):
                if val[i-1] != val[i]:
                    temp = temp *10 + count
                    temp = temp *10 + int(val[i-1])
                    count = 0
                count += 1
            n -= 1
        return str(temp)
            
        