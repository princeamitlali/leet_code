class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # allowed.sort()
        c = 0
        for i in words:
            i = set(i)
            flag = True
            for j in i:
                if j not in allowed:
                    flag = False
                    break
            if flag:
                c += 1
        return c
        