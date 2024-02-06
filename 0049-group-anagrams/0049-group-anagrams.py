class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for i in strs:
            s = "".join(sorted(i))
            r = di.get(s,[])
            r.append(i)
            di[s] = r
        res = []
        for value in di.values():
            res.append(value)
        return res
            