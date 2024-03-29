from collections import deque
class RecentCounter:

    def __init__(self):
        # self.element = []
        self.que = deque()
        

    def ping(self, t: int) -> int:
        # self.element.append(t)
        # c = 0
        # i = len(self.element) -1
        # while i >-1 and self.element[i] >= t-3000:
        #     c += 1
        #     i -= 1
        # return c
        self.que.append(t)
        while self.que and self.que[0] < t - 3000:
            self.que.popleft()
        return len(self.que)
                
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)