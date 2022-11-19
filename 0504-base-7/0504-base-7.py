class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = 1
        if num  < 0:
            sign = -1
            num = - num
        st = ''
        while num > 0:
            st += str(num%7)
            num = num //7
            
        return str(sign * int(st[::-1]))
        