class Solution:
    def minTimeToType(self, word: str) -> int:
        pre = 0
        s = 0
        for i in word:
            ch = ord(i)-97
            v = ch
            ch -= pre
            ch = abs(ch)
            # print(ch)
            ch = min(abs(ch-0),abs(26 - ch))
            s += ch
            pre = v
            
        return s + len(word)
        