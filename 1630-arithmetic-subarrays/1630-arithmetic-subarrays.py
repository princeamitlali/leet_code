class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        sol = []
        for i in zip(l,r):
            v = nums[i[0]:i[1]+1]
            v.sort()
            # print(v)
            res = v[1]-v[0]
            for j in range(len(v)-1):
                if v[j+1] - v[j] != res:
                    sol.append(False)
                    break
                if j == len(v)-2:
                    sol.append(True)
        return sol
                    
                    
        