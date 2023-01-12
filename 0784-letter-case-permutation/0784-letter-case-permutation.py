class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # res = []
        # for i in range(len(s)):
        #     if s[i] not in ["1","2","3","4","5","6","7","8","9","0"]:
        #         v1 = s[:i] + s[i].lower() + s[i+1:]
        #         res.append(v1)
        #         v1 = s[:i] + s[i].upper() + s[i+1:]
        #         res.append(v1)
        # return res
        output=[""]
        for c in s:
            t=[]
            if c.isalpha():
                for o in output:
                    t.append(o+c.upper())
                    t.append(o+c.lower())
            else:
                for o in output:
                    t.append(o+c)
            output=t
        return output
        