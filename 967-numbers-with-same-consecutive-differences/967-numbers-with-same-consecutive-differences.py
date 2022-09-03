class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        temp = []
        def helper(cur,pos,val):
            if pos == n-1:
                temp.append(cur)
                return
            va = val + k
            
            if va <10:
                helper((cur*10)+va,pos+1,va)
            va = val -k
            
            if va >=0 and k!= 0:
                helper((cur*10)+va,pos +1, va)
                
        for i in range(1,10):
            helper(i,0,i)
        return temp
            
       
        # start = pow(10,n-1)
#         end = pow(10,n)
#         print(start,end)
#         temp = []
#         for i in range(start,end,k):
#             val = str(i)
#             ex = True
#             for j in range(len(val)-1):
#                 fir = int(val[j])
#                 sec = int(val[j+1])
#                 if fir - sec == k or sec-fir == k:
#                     pass
#                 else:
#                     ex = False
#                 if
#             if ex:
#                 temp.append(i)

#         return temp
        
        