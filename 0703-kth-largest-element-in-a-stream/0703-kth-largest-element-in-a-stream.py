class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = sorted(nums)
        self.id = k
        

    def add(self, val: int) -> int:
        
        self.arr.append(val)
        self.arr.sort()
        # print(self.arr)
        return self.arr[-self.id]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)