# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        val = guess(high)
        if val == 0:
            return high
        val = guess(low)
        if val == 0:
            return low
        
        while True:
            mid = (high + low) //2
            val = guess(mid)
            if val == 0:
                return mid
            if val == -1:
                high = mid
            else:
                low = mid
                
        
        
        