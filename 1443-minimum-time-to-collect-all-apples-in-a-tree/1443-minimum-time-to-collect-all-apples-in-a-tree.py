class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        parents=[-1]*n
        for edge in edges:
            parent,child=edge
            if parents[child]==-1:
                parents[child]=parent  
            else:
                parents[parent]=child   
        for h in range(n-1,0,-1):
            if hasApple[h] and parents[h]!=-1:
                hasApple[parents[h]]=True
        return sum(hasApple[1:])*2
        