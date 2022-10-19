class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = [s[y-k:y] for y in range(k,len(s)+k,k)]
        rev = True
        s = ""
        for i in res:
            if rev :
                s += i[::-1]
                rev = False
            else:
                s += i
                rev = True
        return s
                
        