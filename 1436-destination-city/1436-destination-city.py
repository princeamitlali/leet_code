class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start,end = [],[]
        for i in paths:
            start.append(i[0])
            end.append(i[1])
        for i in end:
            if i not in start:
                return i
        