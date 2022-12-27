class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len (rocks)
        s = 0
        for i in range(n):
            capacity[i] -= rocks[i]
            
        # print(capacity)
        
        capacity.sort()
        print(capacity)
        for i in range(n):
            s += capacity[i]
            if s > additionalRocks:
                return i 
        return n