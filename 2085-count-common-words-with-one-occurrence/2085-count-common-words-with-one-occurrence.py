class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res1 = []
        for i in words1:
            if words1.count(i) == 1:
                res1.append(i)
        print(res1)
        res2 = []
        for i in words2:
            if words2.count(i) == 1:
                res2.append(i)
        print(res2)
        c = 0
        for i in res1:
            if i in res2:
                c += 1
        
        return c
        