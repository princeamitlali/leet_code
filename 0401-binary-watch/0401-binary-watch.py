class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
#         li = [0.01,0.02,0.04,0.08,0.16,0.32,1.00,2.00,4.00,8.00]
#         n = len(li)
#         temp = []
#         for i in range(1,n):
#             for j in range(i,n):
#                 temp.append(li[i]+li[j])
#         for i in range(len(temp)):
#             temp[i] = str(temp[i]).replace(".",":")
#         return []
        
        res=[]
        for hour in range(12):
            for minutes in range(60):
                if bin(hour)[2:].count('1')+bin(minutes)[2:].count('1') ==turnedOn:
                        y= '{}:{}'.format(hour,str(minutes).zfill(2))
                        res.append(y)
        return res