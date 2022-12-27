class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = ""
        for i in s:
            if i.isupper():
                if i.lower() in s:
                    m = max(m,i)
            # else:
            #     if i.upper() in s:
            #         m = max(m,i.upper())
       
            
        return m