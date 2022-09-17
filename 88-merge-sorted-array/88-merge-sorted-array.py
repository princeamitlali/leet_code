class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        if n==0:
            pass
        else:
            curr = 0
            for i in range(m+n):
                if i < m+n and curr < n:
                    if nums1[i] >= nums2[curr]:
                        nums1.insert(i,nums2[curr])
                        nums1.pop(-1)
                        curr += 1
            ind = -1
            nums2 = nums2[curr:]
            if curr < n:
                for i in nums2[::-1]:
                    nums1[ind] = i
                    ind -= 1
                
        