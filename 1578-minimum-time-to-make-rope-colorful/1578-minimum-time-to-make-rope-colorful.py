class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost = 0
        for i in range(len(colors) - 1):
            c1, c2 = colors[i : i+2]
            t1, t2 = neededTime[i : i+2]
            
            if c1 == c2:
                cost += min(t1, t2)
                neededTime[i+1] = max(t1,t2)
                
        return cost
        