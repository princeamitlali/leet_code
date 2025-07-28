class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1

        dic = sorted(dic.items())
        ans = 0  
        for i in range(len(dic)-1):
            if dic[i+1][0] - dic[i][0] == 1:
                ans = max(ans, dic[i][1] + dic[i+1][1])
        return ans  