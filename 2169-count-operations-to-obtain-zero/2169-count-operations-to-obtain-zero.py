class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while True:
            if num1 == 0:
                break
            if num2 == 0:
                break
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1
            print(num1,num2)
        return count