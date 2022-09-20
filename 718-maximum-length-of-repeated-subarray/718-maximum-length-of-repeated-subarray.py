class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums2 = "".join([chr(x)for x in nums2])
        max_str = ""
        ans = 0
        for num in nums1:
            max_str += chr(num)
            if max_str in nums2:
                ans = max(len(max_str),ans)
            else:
                max_str = max_str[1:]
        return ans
#         # print(nums1,nums2)
#         n = len(nums1)
#         temp1 =  []
#         count = 0
#         def get_sub(li):
#             temp = []
#             n = len(li)
#             for i in range(n):
#                 for j in range(i,n):
#                     temp.append(li[i:j+1])
#             return temp
#         l1 = get_sub(nums1)
#         # l2 = get_sub(nums2)
#         m = len(nums2)
#         for i in range(m):
#             # l1 = get_sub(i,nums1)
#             for j in range(i,m):
#                 if nums2[i:j+1] in l1:
#                     if len(nums2[i:j+1]) > count:
#                         count = len(nums2[i:j+1])
        
#         return count
        