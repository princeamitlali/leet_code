class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        v = garbage[0]
        pp,gp,mp = 0,0,0
        p,g,m = v.count("P"),v.count("G"),v.count("M")
        for i in range(1,len(garbage)):
            # print(p,g,m)
            r = travel[i-1]
            v = garbage[i]
            if "P" in v:
                p += pp + r
                p += v.count("P")
                pp = 0
            else:
                pp += r
            
            if "G" in v:
                g += gp + r
                g += v.count("G")
                gp = 0
            else:
                gp += r
                
            if "M" in v:
                m += mp + r
                m += v.count("M")
                mp = 0
            else:
                mp += r
        # print(p,g,m)
        return p+g+m
        