class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word += "x"
        pre = ""
        c = 0
        res = []
        for i in word:
            if i in ["1","2","3","4","5","6","7","8","9","0"]:
                c *= 10
                c += int(i)
            else:
                if c > 0:
                    res.append(c)
                    c = 0
                else:
                    if pre == "0":
                        res.append(0)
            pre = i
        print(res)
        return len(set(res))
        