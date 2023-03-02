class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        for i,val in enumerate(groupSizes):
            # print(i,val)
            if val not in dic:
                dic[val] = [i]
            else:
                v = dic[val]
                v.append(i)
                # print(v)
                dic[val] = v
        res = []
        for i in dic:
            val = dic[i]
            for j in range(0,len(val),i):
                res.append(val[j:j+i])
        return res