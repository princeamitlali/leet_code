class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hm,vm = 0,0
        for i in moves:
            print(i)
            if i == "U":
                vm +=1
            if i == "D":
                vm -=1
            if i == "R":
                hm += 1
            if i == "L":
                hm -= 1
        # print(vm,hm)
        return hm == 0 and vm == 0
        