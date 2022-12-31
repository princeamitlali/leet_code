class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i in nums2 or i in nums3:
                res.append(i)
        for i in nums2:
            if i in nums3:
                res.append(i)
        return list(set(res))
        