class Solution:
    def fillCups(self, amount: List[int]) -> int:
        n = sum(amount) //2
        flag = True
        for i in amount:
            if i > n:
                flag = False
        if flag:
            if sum(amount) %2 == 0:
                return n
            else:
                return n+1
        return max(amount)
        