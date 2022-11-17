import math
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(65, 92)]
        st = ''
        while columnNumber > 0:
            r = (columnNumber-1) % 26
            columnNumber = (columnNumber-1) //26
            st += capitals[r]

        return st[::-1]
        
        