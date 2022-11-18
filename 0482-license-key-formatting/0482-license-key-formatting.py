class Solution:
    def licenseKeyFormatting(self, s: str, val: int) -> str:
        i = s.replace("-",'').upper()[::-1]
        print(i)
        l = len(i)
        st =  0
        t = ''
        while l > val:
            t += i[st:st + val] + '-'
            st += val
            l -= val
            # print(st,l,t)

        if l<= val:
            t  += i[st:]
        return t[::-1]
        