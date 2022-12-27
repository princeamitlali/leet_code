class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = 64
        for i in s:
            # print(ord(i))
            if i.isupper():
                if i.lower() in s:
                    # print(ord(i))
                    m = max(m,ord(i))
            else:
                if i.upper() in s:
                    # print(ord(i.upper()))
                    m = max(m,ord(i.upper()))
            # print(m)
        if m < 65:
            return ""
            
        return chr(m)