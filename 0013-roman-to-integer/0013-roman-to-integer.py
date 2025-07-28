class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        pre = 0
        sumi = 0
        for i in s:
            val = dic[i]
            sumi += val
            if pre < val:
                sumi -= pre * 2
            pre = val
        return sumi