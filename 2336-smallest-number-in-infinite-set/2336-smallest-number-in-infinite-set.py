class SmallestInfiniteSet:

    def __init__(self):
        self.set = [i for i in range(1,1001)]
        

    def popSmallest(self) -> int:
        if len(self.set)>0:
            return self.set.pop(self.set.index((min(self.set))))
        
        
        

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.append(num)
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)