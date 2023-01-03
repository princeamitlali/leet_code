class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res1 = []
        words1 = s1.split(" ")
        words2 = s2.split(" ")
        for i in words1:
            if words1.count(i) == 1:
                res1.append(i)
        print(res1)
        res2 = []
        for i in words2:
            if words2.count(i) == 1:
                res2.append(i)
        print(res2)
        c = []
        for i in res1:
            if i not in words2:
                c.append(i)
        for i in res2:
            if i not in words1:
                c.append(i)
        
        return list(set(c))