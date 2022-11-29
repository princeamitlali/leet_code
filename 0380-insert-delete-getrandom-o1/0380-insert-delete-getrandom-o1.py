class RandomizedSet:

    def __init__(self):
        self.storage = dict() # 
        self.MODULO = 1000
        self.vals = []
        

    def insert(self, val: int) -> bool:
        if val in self.storage:
            return False
        else:
            self.storage[val] = len(self.vals)
            self.vals.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.storage:
            index_of_removal = self.storage[val]
            self.vals[index_of_removal] = self.vals[-1]
            self.storage[self.vals[-1]] = index_of_removal
            self.vals.pop()
            del self.storage[val]
            
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()