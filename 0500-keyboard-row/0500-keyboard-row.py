class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        val = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        temp = []
        for word in words:
            # print(word)
            c = []
            for i in word:
                i = i.lower()
                if i in val[0]:
                    c.append(1)
                if i in val[1]:
                    c.append(2)
                if i in val[2]:
                    c.append(3)
            # print(c)
            if len(set(c)) == 1:
                temp.append(word)
                    
                    
            # if word in val[0] or word in val[1] or word in val[2]:
            #     print(word)
            #     temp.append(word)
        return temp
                