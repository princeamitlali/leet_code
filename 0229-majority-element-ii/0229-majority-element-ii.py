class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # if len(nums) == 1:
        #     return nums
        threshold = len(nums)//3
        dic = {}
        res = []
        for i in nums:
            dic[i] = dic.get(i,0)+1
            if dic[i] > threshold:
                res.append(i)
        # print(dic)
        return list(set(res))
        