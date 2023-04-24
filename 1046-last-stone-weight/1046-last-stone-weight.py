class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            v1 = stones.pop()
            v2 = stones.pop()
            if v1 != v2:
                diff = abs(v1-v2)
                stones.append(diff)
        
        if len(stones) == 0:
            return 0
        return stones[0]