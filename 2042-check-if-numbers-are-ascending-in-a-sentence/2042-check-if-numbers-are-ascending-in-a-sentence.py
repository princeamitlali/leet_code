class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        res = []
        s = s.split(" ")
        for i in s:
            try:
                v  = int(i)
                res.append(v)
                # print(v)
            except:
                continue
        return sorted(res) == res and len(res) == len(set(res))
        