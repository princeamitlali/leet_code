class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        p,n=[],[]
        for i in nums:
            if i %2 == 0:
                p.append(i)
            else:
                n.append(i)
        nums = []
        for i in zip(p,n):
            nums.append(i[0])
            nums.append(i[1])
        return nums
        