class StockSpanner:

    def __init__(self):
        self.stack = []
        self.count = 0
        

    def next(self, price: int) -> int:
        # print(price)
        self.count += 1
        i = len(self.stack)


        while i >0 and self.stack[-1][0] <= price:
            self.stack.pop()
            i -= 1
        self.stack.append([price,self.count])
        # print(len(self.stack))
        if i == 0:
            
            return self.count 
        else:
            return self.count - self.stack[-2][1]

            

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)