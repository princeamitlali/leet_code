class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic = {}
        for i in logs:
            key = str(i[0])
            val = i[1]
            if key in dic.keys():
                if val in dic[key]:
                    continue
                else:
                    v = dic[key]
                    v.append(val)
                    dic[key] = v
            else:
                dic[key] = [val]
        res = [0 for i in range(k)]
        for i in dic:
            v = len(dic[i])
            res[v-1] +=1
        
        return res
        