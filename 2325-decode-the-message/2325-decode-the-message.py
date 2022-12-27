class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        key = "".join(key.split(" "))
        print(key)
        dic = {}
        c = 0
        for k in key:
            # k = str(key[i])
            k = str(k)
            if k not in dic.keys():
                dic[k] = chr(c+97)
                c += 1
            if c == 27:
                break
        res = ""
        for i in message:
            if i != " ":
                i = dic[str(i)]
            res += i
        return res
                
        