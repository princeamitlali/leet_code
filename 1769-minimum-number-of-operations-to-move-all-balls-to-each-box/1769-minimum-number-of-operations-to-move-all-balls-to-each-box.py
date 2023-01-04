class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indexes = []
        
        for i in range(len(boxes)):
            if boxes[i] == "1":
                indexes.append(i)
        res = []       
        for i in range(len(boxes)):
            c = 0
            for ind in indexes:
                c += abs(ind-i)
            res.append(c)
                
        print(boxes)
         
        return res
                       
        