class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        r1,r2 = s[0] ,s[3] 
        c1,c2 = s[1], s[4] 
        res = []
        for i in range(ord(r1),ord(r2)+1):
            i = chr(i)
            for j in range(int(c1),int(c2)+1):
                res.append(i+str(j))
        return res
                
        