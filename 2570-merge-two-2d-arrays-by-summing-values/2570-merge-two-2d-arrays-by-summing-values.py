class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = {}
        for i in nums1:
            dic[i[0]] = dic.get(i[0],0) + i[1]
        for i in nums2:
            dic[i[0]] = dic.get(i[0],0) + i[1]
        res = []
        for i in sorted(dic.items(),key = lambda x:x[0]):
            res.append([i[0],i[1]])
        return res