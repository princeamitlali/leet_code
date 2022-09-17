class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        su = 0
        columnTitle = columnTitle[::-1]
        for i in range(len(columnTitle)):
            mul = pow(26,i)
            su += (ord(columnTitle[i]) -64) * mul
        return su
            
        