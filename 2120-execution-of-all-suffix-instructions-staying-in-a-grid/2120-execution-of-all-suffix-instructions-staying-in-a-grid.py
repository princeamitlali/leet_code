class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        
        res = []
        for j in range(len(s)):
            r = 0
            x,y = startPos[0],startPos[1]
            # print("pass",j)
            for i in s[j:]:
                # print(i,x,y)
                if i =="R":
                    y += 1

                if i == "L":
                    y -= 1

                if i == "U":
                    x -= 1

                if i == "D":
                    x += 1
                if x <0 or x>n-1 or y <0 or y >n-1:
                    break
                r += 1
            res.append(r)
                
            # print(r,x,y)
        return res
                
                
            
        