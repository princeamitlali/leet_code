from collections import Counter
class Solution:
    def countAndSay(self, n: int) -> str:
        c = Counter
        temp = 1
        val = 0
        if n == 1:
            return "1"
        while n > 1:
            count = 1
            val = str(temp)
            print("v",val)
            dic = c(val)
            temp = 0
            if len(val) == 1:
                temp = 10 + int(val)
            else:
                temp = 0
                val = val + "."
                for i in range(1,len(val)):
                    if val[i-1] != val[i]:
                        # print("c",count,val[i-1])
                        temp = temp *10 + count
                        temp = temp *10 + int(val[i-1])
                        count = 1
                    else:
                        count += 1
                # if count > 0:
                #     temp = temp *10 + count -1
                #     temp = temp *10 + int(val[-1])
                    
                    
            # for i in dic:  
            #     temp = temp *10 + dic[i]
            #     temp = temp * 10 + int(i)
            n -= 1
        return str(temp)
            
        