class Solution:
    def replaceDigits(self, s: str) -> str:
        n = len(s)
        if n %2 == 1:
            n -= 1
        for i in range(0,n,2):
            s  = s[:i+1] + chr(ord(s[i])+int(s[i+1])) + s[i+2:]
            
        return s
        