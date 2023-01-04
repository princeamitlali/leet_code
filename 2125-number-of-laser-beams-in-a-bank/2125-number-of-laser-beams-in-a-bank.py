class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = []
        for i in bank:
            v = i.count("1")
            if v > 0:
                res.append(v) 
        # print(res)
        r = 0
        for i in range(len(res)-1):
            r += res[i] * res[i+1]
    
        return r
        