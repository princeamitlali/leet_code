class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            v = sum(list(map(int, str(i).strip())))
            if v in dic.keys():
                val = dic[v]
                val.append(i)
                dic[v] = val
            else:
                dic[v] = [i]
        print(dic)
        res = -1
        for i in dic:
            v = dic[i]
            if len(v) == 1:
                continue
            v.sort()
            res = max(res,v[-1]+v[-2])
        return res
        