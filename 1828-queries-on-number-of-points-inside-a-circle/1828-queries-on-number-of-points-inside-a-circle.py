class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for i in queries:
            
            count = 0
            for j in points:
                x = j[0] - i[0]
                y = j[1] - i[1]
                if math.sqrt((x*x) + (y*y)) <= i[2]:
                    count += 1
            res.append(count)
        return res
                    
        