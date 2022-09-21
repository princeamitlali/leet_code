class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        resLen = 0

        for i in range(len(s)):

            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:

                if (r - l + 1) > resLen:

                    res = s[l : r + 1]

                    resLen = r - l + 1

                l -= 1

                r += 1

            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:

                if (r - l + 1) > resLen:

                    res = s[l : r + 1]

                    resLen = r - l + 1

                l -= 1

                r += 1

        return res
        # res = ""
        # temp = []
        # def traverse(st,res):
        #     # print(st)
        #     if len(st)  >1 and res == "":
        #         if st == st[::-1]:
        #             res = st
        #             return st
        #         left,right = "",""
        #         if st[:-1] not in temp:
        #             temp.append(st[:-1])
        #             left = traverse(st[:-1],res)
        #         if st[1:] not in temp:
        #             temp.append(st[1:])
        #             right = traverse(st[1:],res)
        #         if len(left) > len(right):
        #             return left
        #         return right
        #     else:
        #         return st[0]
        # val = traverse(s,res)
        # # print(val)
        # return val
        
            
        