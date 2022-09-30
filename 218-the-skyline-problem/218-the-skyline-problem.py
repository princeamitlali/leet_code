class Solution:
    def getSkyline(self, b: List[List[int]]) -> List[List[int]]:
        
        events = [(l,-h,r) for (l,r,h) in b]
        events +=[(r,0,0)for(_,r,_) in b]
        events.sort()
        
        ans = [[0,0]]
        live = [[0,float("inf")]]
        
        for (l,negh,r) in events:
            while live[0][1] <= l:
                heapq.heappop(live)
            if negh:
                heapq.heappush(live,[negh,r])
            if ans[-1][1] != -live[0][0] :
                ans.append((l,-live[0][0]))
        return ans[1:]
            
            
        