class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        v = ord(coordinates[0])-96
        v += int(coordinates[1])
        print(v)
        return v % 2 == 1
        
        