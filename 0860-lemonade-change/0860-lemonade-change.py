class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        temp = [0,0,0]
        for i in bills:
            if i == 5:
                temp[0] = temp[0] +1
            elif i == 10:
                temp[1] = temp[1] + 1
                if temp[0] > 0:
                    temp[0] = temp[0] - 1
                else:
                    return False
            elif i == 15:
                temp[2] = temp[2] + 1
                if temp[1] > 0:
                    temp[1] = temp[1] - 1
                elif temp[0] > 1:
                    temp[0] = temp[0] -2
                else:
                    return False
            else:
                if temp[2] > 0:
                    temp[2] = temp[2] - 1
                elif temp[1] > 0 and temp[0] > 0:
                    temp[0] = temp[0] -1
                    temp[1] = temp[1] -1
                elif temp[0] > 2:
                    temp[0] = temp[0] -3
                else:
                    return False
        return True
                
        