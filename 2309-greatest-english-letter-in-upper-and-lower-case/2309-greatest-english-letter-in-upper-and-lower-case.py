class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = ""
        for i in s:
            # print(ord(i))
            if i.isupper():
                if i.lower() in s:
                    # print(ord(i))
                    m = max(m,i)
            else:
                if i.upper() in s:
                    # print(ord(i.upper()))
                    m = max(m,i.upper())
            # print(m)
       
            
        return m