class OrderedStream:

    def __init__(self, n: int):
        self.pairs = {}
        self.pointer = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.pairs[idKey] = value

        temp = list()
        while self.pointer + 1 in self.pairs:
            self.pointer += 1

            temp.append(self.pairs[self.pointer])

        return temp


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)