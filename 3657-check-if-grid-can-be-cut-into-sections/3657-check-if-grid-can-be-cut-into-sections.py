class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        verticals = []
        horizontals = []
        for i in rectangles:
            verticals.append([i[0],i[2]])
            horizontals.append([i[1],i[3]])
        verticals.sort(key = lambda x:x[0])
        horizontals.sort(key = lambda x: x[0])
        h_cut,v_cut,h_end,v_end = 0,0,0,0
        for i in range(len(verticals)):
            start_v, end_v = verticals[i]
            start_h,end_h = horizontals[i]
            if start_v >= v_end:
                v_end = end_v
                v_cut +=1
            v_end = max(end_v,v_end)
            if v_cut >2:
                return True
            if start_h >= h_end:
                h_cut += 1
                h_end = end_h
            h_end = max(h_end,end_h)
            if h_cut >2:
                return True
        return False

        
            
        