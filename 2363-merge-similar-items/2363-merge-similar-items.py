class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = {}
        for i in items1:
            if i[0] in dic.keys():
                dic[i[0]] += i[1]
            else:
                dic[i[0]] = i[1]
        for i in items2:
            if i[0] in dic.keys():
                dic[i[0]] += i[1]
            else:
                dic[i[0]] = i[1]
        dic = sorted(dic.items(), key = lambda x:x[0])
        items1 = []
        for i in dic:
            items1.append(list(i))
        return items1
        