class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count1 = 0 
        count2 = 0
        left = 0
        li = ['a','e','i','o','u','A','E','I','O','U']
        right = len(s)-1
        while right > left:
            if s[right] in li:
                count1 += 1
            if s[left] in li:
                count2 += 1
            right -= 1
            left += 1
        return count1 == count2
        