class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
#         piles.sort()
#         n = len(piles)
#         if n == 1:
#             v = piles[0]
#             while k >0 and v > 0:
#                 v =  math.ceil(v / 2)
#                 k -= 1
#             return v

#         for i in range(k):
            
#             v =  math.ceil(piles.pop() / 2)
#             j = 0
#             while j < (n -1) and piles[j] < v :
#                 j += 1
#             piles.insert(j,v)
#             # print(piles)
#         return sum(piles)

        max_heap = []

        for pile in piles:
            heapq.heappush(max_heap, -pile)

        while k != 0:
            stone = heapq.heappop(max_heap)
            stone = math.ceil(stone * -1 / 2)
            heapq.heappush(max_heap, -stone)
            k -= 1

        return -sum(max_heap)
        