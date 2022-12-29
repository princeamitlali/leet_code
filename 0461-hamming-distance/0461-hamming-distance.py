from math import ceil
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        x = bin(x)[2:]
        y = bin(y)[2:]
        lx = len(x)
        ly = len(y)
        if lx> ly:
            diff = lx - ly
            y = "0" * diff + y
            
        else:
            diff = ly - lx
            x = "0" * diff + x
            lx += diff
        for i in range(lx):
            if x[i] != y[i]:
                count += 1
                
        return count 
        