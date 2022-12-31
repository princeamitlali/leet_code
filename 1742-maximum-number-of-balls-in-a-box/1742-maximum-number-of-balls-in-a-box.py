class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dic = {}
        for i in range(lowLimit,highLimit+1):
            v = sum([int(j) for j in str(i)])
            if v in dic.keys():
                dic[v] += 1
            else:
                dic[v] = 1
        print(dic)
        m = 0
        for i in dic:
            m = max(m,dic[i])
        return m
        