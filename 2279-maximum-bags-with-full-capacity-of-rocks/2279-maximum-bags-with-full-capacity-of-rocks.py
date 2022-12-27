class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len (rocks)
        s = 0
        for i in range(n):
            capacity[i] -= rocks[i]
            
        capacity.sort()
        if capacity[0] > additionalRocks:
            return 0
        if sum(capacity) < additionalRocks:
            return n
        for i in range(n):
            s += capacity[i]
            if s > additionalRocks:
                return i 
        return n