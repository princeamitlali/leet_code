import math
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if len(s) == 0:
            return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in ('-','+'):
            s = s[1:]
        res = 0
        for i in s:
            if i.isdigit():
                res = res * 10 + int(i)
            else:
                break
        res = sign * res
        if res < -2147483648:
            return -2147483648
        elif res >= 2147483647:
            return 2147483647
        return res   
            
        