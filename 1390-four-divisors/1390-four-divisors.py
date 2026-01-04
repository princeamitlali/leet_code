import math
class Solution:
    def is_four_divisor(self,n):
        div_count = 2
        s = 1 + n
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                div_count -= 1
                s += i
                if n/i != i:
                    div_count -= 1
                    s += n/i
        if div_count == 0:
            return int(s)
        return 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        s = 0
        
        for i in nums:
            s += self.is_four_divisor(i)
        return s
        