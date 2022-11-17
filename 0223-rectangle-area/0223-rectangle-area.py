class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        l1 = ax1-ax2
        l2 = bx1-bx2
        b1 = ay2-ay1
        b2 = by2 - by1
        a1 = abs(l1*b1)
        a2 = abs(l2*b2)
        print(a1+a2)
        cx = max(min(ax2,bx2)-max(ax1,bx1), 0)
        cy = max(min(ay2,by2)-max(ay1,by1), 0)
        ca = abs(cx * cy)
        print(ca)
        return a1 + a2 - ca
        