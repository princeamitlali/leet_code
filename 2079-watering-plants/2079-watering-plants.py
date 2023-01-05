class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        n = len(plants)
        cap = capacity
        for i in range(len(plants)):
            if cap - plants[i] <0:
                cap = capacity 
                res += 2 * (i)
            cap -= plants[i]
            # print(res)
        # print(res)
        return res + n
                
        