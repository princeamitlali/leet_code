class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        res = []
        if len(nums2) < len(nums1):
            nums1,nums2 = nums2,nums1
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                res.append(nums2[i])
        return res