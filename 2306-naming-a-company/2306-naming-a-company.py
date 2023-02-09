class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # n = len(ideas)
        # count = 0
        # for i in range(n-1):
        #     v = ideas[i]
        #     for j in ideas[i+1:]:
        #         if v[1:] != j[1:]:
        #             if v[0]+j[1:] not in ideas and j[0]+v[1:] not in ideas:
        #                 # print(v,j)
        #                 count +=2
        # return count
        ss = [set() for _ in range(26)]
        for s in ideas:
            c = ord(s[0]) - ord('a')
            tail = s[1:]
            ss[c].add(tail)

        ans = 0
        for i in range(26):
            for j in range(26):
                if i == j: continue
                a = len(ss[i] - ss[j])
                b = len(ss[j] - ss[i])
                ans += a * b
        return ans
                    
        