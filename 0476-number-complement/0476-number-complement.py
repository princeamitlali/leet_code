class Solution:
    def findComplement(self, num: int) -> int:
        st = ""
        for i in bin(num)[2:]:
            if i == '0':
                st += "1"
            else:
                st += "0"
        return (int(st,2))
        