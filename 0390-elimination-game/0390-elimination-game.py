class Solution:
    def lastRemaining(self, n: int) -> int:
#         val = [i+1 for i in range(n)]
#         c = 0
#         while len(val) >1:
#             res = []
#             c += 1
#             for i in range(1,len(val),2):
#                 res.append(val[i])
#             val = res[::-1]
#             # print(val,sqrt(log2(val[i])))
#         print(val[0],c)
#         return val[0]
        if n == 1:
            return 1
        return 2 * (n // 2 - self.lastRemaining(n // 2) + 1)
        