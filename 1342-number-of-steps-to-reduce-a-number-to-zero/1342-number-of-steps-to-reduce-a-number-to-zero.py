class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0
        for i in str(bin(num))[2:]:
            # print(i)
            if i == "0":
                c +=1
            if i == "1":
                c += 2
        print(bin(num))
        return c-1
        