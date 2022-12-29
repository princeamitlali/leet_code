from math import ceil
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #convert to binary and check where bits not equal
        count = 0
        x = bin(x)[2:]
        y = bin(y)[2:]
        # print(x,y)
        lx = len(x)
        ly = len(y)
        if lx> ly:
            diff = lx - ly
            y = "0" * diff + y
            
        else:
            diff = ly - lx
            x = "0" * diff + x
        print(x,y)
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
                
        return count 
        