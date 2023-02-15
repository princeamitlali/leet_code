class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32
        val = '0123456789abcdef'
        res = ""
        while num > 0:
            
            res += val[num%16]
            num //=16
        return res[::-1]
            
            
            
        # return hex(num)[2:]
        