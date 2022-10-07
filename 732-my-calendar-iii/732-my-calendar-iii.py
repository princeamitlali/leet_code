from bisect import bisect_left,bisect_right
class MyCalendarThree:

    def __init__(self):
        self.events = []
        self.bks = []
        self.maxbk = 0

    def book(self, start: int, end: int) -> int:
        s = bisect_right(self.events, start)
        self.events.insert(s, start)
        if s > 0:
            self.bks.insert(s, self.bks[s-1]+1)
            self.maxbk = max(self.maxbk, self.bks[s-1]+1)
        else:
            self.bks.insert(0, 1)
            self.maxbk = max(self.maxbk, 1)
        e = bisect_left(self.events, end)
        for i in range(s+1, e):
            self.bks[i] += 1
            self.maxbk = max(self.maxbk, self.bks[i])
        self.events.insert(e, end)
        self.bks.insert(e, self.bks[e-1]-1)
        return self.maxbk
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)