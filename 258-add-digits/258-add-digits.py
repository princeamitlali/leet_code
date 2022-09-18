class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) >1:
            su = 0
            for i in num:
                su += int(i)
            num = str(su)
        return int(num)