class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gp,cp = 0,0
        while gp <len(g) and cp < len(s):
            if g[gp] > s[cp]:
                cp += 1
            else:
                cp += 1
                gp += 1
        return gp 