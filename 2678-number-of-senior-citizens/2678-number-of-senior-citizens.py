class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        for i in details:
            val = i[11:13]
            if int(val) > 60:
                c += 1
        return c
        