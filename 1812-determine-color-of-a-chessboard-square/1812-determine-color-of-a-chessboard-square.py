class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        v = ord(coordinates[0])-96
        v += int(coordinates[1])
        return v % 2 == 1
        
        