class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy = {}
        for i in strs:
            v = ''.join(sorted(i))
            if v not in copy.keys():
                copy.update({v:[i]})
            else:
                val = copy[v]
                val.append(i)
                copy.update({v:val})
        res = []
        for i in copy:
            res.append(copy[i])
        return res