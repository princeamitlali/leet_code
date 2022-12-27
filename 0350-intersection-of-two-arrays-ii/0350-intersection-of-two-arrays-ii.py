
# import counter class from collections module
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter
        dic1 = c(nums1)
        dic2 = c(nums2)
        # print(dic1,dic2)
        res = []
        for i in dic1:
            if i in dic2.keys():
                for j in range(min(dic1[i],dic2[i])):
                    res.append(i)
        return res