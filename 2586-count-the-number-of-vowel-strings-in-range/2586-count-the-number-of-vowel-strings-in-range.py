class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        c = 0
        for i in range(left,right+1):
            v = words[i]
            if v[0] in ['a','e','i','o','u'] and v[-1] in ['a','e','i','o','u']:
                c += 1
        return c