class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        # print(verticalCuts,horizontalCuts)
        rh,rw = 0,0
        for i in range(len(horizontalCuts)-1):
            rh = max(rh,horizontalCuts[i+1]-horizontalCuts[i] )
            # print(rh)
        # print("ds")
        for i in range(len(verticalCuts)-1):
            rw = max(rw,verticalCuts[i+1]-verticalCuts[i] )
            # print(rw)
        
        return (rh * rw) % 1000000007
        