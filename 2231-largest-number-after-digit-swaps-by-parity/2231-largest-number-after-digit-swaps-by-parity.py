class Solution:
    def largestInteger(self, num: int) -> int:
        p,n="",""
        num = str(num)
        for i in num:
            if int(i) %2 == 0:
                p += i
            else:
                n += i
        p = sorted(p)
        n = sorted(n)
        
        for i in range(len(num)):
            if int(num[i]) %2 == 0:
                num = num[:i] + str(p.pop())+ num[i+1:]
            else:
                num = num[:i] + str(n.pop())+ num[i+1:]
        
        return int(num)
        