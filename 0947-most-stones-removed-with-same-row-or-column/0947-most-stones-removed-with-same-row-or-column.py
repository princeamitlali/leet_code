class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def removeIsland(i,j):
            inIsland = [] # stones in the same island
            ind = 0 # index to traverse stones
            while ind < len(stones):
                x,y = stones[ind] # this stone
                if x == i or y == j: # if it is in the same row or col
                    inIsland.append(stones.pop(ind)) # it is in the island –– pop from stones and add to inIsland
                else: # otherwise
                    ind += 1 # move to the next index in stones
            for stone in inIsland: # for all the stones connected to this one
                removeIsland(*stone) # recursively remove the rest of the island which connects to the stone
        ans = len(stones) # we start off assuming that we can remove every stone
        while stones: # while there are stones left to remove
            removeIsland(*stones.pop()) # remove the island connected to the last stone
            ans -= 1 # one stone from this island must remain
        return ans