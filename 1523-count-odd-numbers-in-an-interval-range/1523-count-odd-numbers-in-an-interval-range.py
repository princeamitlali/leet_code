class Solution:
    def countOdds(self, low: int, high: int) -> int:
        v = high - low
        if v == 1:
            return 1
        if (v) %2 == 0:
            if low %2 == 1:
                return 1 + v //2
            else:
                return v //2
        else:
            return (v+1)//2
        