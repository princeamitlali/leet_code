class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        temp = []
        su = 0
        for num in nums:
            if num %2 == 0:
                su += num
            
        for query in queries:
            val = nums[query[1]]
            nums[query[1]] = nums[query[1]] + query[0]
            if nums[query[1]] % 2 == 0:
                if val %2 == 0:
                    su += query[0]
                else:
                    su += nums[query[1]]
            else:
                if val %2 == 0:
                    su -= val
            
            # print(nums)
            # su = 0
            # for num in nums:
            #     if num %2 == 0:
            #         su += num
            temp.append(su)
        return temp
        