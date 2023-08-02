class Solution:
    def topKFrequent(self, nums: List[int], k: int) :
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        dic = sorted(dic.items(), key = lambda x:x[1],reverse = True)[:k]
        return [i[0] for i in dic]
            # print(i[1])