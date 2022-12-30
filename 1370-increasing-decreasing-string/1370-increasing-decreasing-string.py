class Solution:
    def sortString(self, s: str) -> str:
        v = sorted(set(s))
        i = 0
        res = ""
        flag = False
        while len(s)>0: 
            for i in v:
                if i in s:
                    res +=i
                    ind = s.index(i)
                    s = s[:ind]+s[ind+1:]
                        
            v = v[::-1]
            # print(s,res)
        return res
                        
        