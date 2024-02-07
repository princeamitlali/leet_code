class Solution:
    def frequencySort(self, s: str) -> str:
        di = {}
        for i in s:
            di[i] = di.get(i,0) + 1
        di = sorted(di.items(), key=lambda item: (-item[1], item[0]))
        # print(di)
        s = ""
        for key,value in di:
            s += key*value
        return s