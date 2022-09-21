class Solution(object):
    def letterCombinations(self, digits):
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if digits =="":
            return []
        temp = [""]
        n = 0
        while n < len(digits):
            val = dic[digits[n]]
            t = []
            for j in temp:
                if len(j) > n:
                    continue
                t.append(j + val[0])
                t.append(j + val[1])
                t.append(j + val[2])
                if val == "pqrs" or val == "wxyz":
                    t.append(j + val[3])
            temp = t
            n += 1
        return temp