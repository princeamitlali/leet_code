class Solution(object):
    def divide(self, dividend, divisor):
        sign = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        def recur_div(a, b):
            if a < b: return 0
            n = 1
            cur = b
            while cur + cur <= a:
                cur += cur
                n += n
            return n + recur_div(a-cur, b)

        n = recur_div(dividend, divisor)

        if sign: 
            return -min(2147483648, n)
        else: 
            return min(2147483647, n)
        
#         count = 1
#         if dividend == 0:
#             return 0
#         flagA = 1
        
#         if dividend < 0:
#             dividend = - dividend
#             flagA *= -1
#         if divisor < 0:
#             divisor = - divisor
#             flagA *= -1
#         div = divisor
#         if divisor > dividend:
#             return 0
#         if divisor == dividend:
#             return flagA*1
#         if flagA*dividend > 2147483646 and divisor == 1:
#             return flagA*2147483647
#         if flagA*dividend < -2147483647 and divisor == 1:
#             return flagA*2147483648
#         while divisor + divisor < dividend:
#             divisor += divisor
#             count += count
#         print(divisor,count)
#         if divisor+ divisor ==  dividend:
#             return flagA*count
#         else:
#             while divisor + div <= dividend:
#                 divisor += div
#                 count += 1
#             print(divisor,count)

#             return flagA*count
            
        
        
#         return flagA*count
        