class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]
        pre = True
        for i in b[1:]:
            if i == "0" and pre is True:
                pre = False
            elif i == "1" and pre is False:
                pre = True
            else:
                return False
        return True
        