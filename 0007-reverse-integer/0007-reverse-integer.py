class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x = -x   
        ans = 0
        while x > 0:
            x,r = x//10,x%10
            ans = ans *10 + r
        if(ans>2**31):
            return 0
        if flag:
            return - ans
        return ans