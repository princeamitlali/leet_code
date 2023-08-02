class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        m = len(v1)
        n = len(v2)
        num1 = ""
        num2 = ""
        for i in range(max(m,n)):
            # print(1,v1[i],v2[i])
            if i < m and int(v1[i]) >0:
                num1 += v1[i].lstrip('0')
                
            else:
                
                num1 += "0"
            if i < n and int(v2[i]) >0 :
                num2 += v2[i].lstrip('0')
                 
            else:
                num2 += "0"
        # print(num1,num2)
            
        num1 = int(num1)
        num2 = int(num2)
            
            
            
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
        return 0
            
        