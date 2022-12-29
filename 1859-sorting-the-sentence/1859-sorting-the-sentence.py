class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        res = [i for i in range(len(s))]
        for i in s:
            res[int(i[-1])-1] = i[:-1]
        return " ".join(res)
        