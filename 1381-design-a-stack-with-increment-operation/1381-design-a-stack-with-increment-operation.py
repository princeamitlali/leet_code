class CustomStack:

    def __init__(self, maxSize: int):
        self.elements = []
        self.size = maxSize
        

    def push(self, x: int) -> None:
        if len(self.elements) < self.size:
            self.elements.append(x)
        

    def pop(self) -> int:
        if len(self.elements) >0:
            return self.elements.pop()
        return -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.elements))):
            self.elements[i] += val
                       
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)