class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        res = []
        for i,val in enumerate(groupSizes):
            if val == 1:
                res.append([i])
                continue
            if val not in dic:
                dic[val] = [i]
            else:
                v = dic[val]
                v.append(i)
                if len(v) == val:
                    res.append(v)
                    v = []
                dic[val] = v
        # res = []
        for i in dic:
            val = dic[i]
            for j in range(0,len(val),i):
                res.append(val[j:j+i])
        return res