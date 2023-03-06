class Solution:
    
        
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def compress(chars):
            chars += "_"
            prev = ""
            count = 0
            res = []
            for i in chars:
                if prev != i:
                    if count > 0:
                        for j in str(count+1):
                            res.append(str(j))

                    res.append(i)
                    count = 0
                    prev = i
                else:
                    count += 1
            return res[:-1]
        res = []
        pl = compress(pattern)
        for i in words:
            if len(set(i)) != len(set(pattern)):
                continue
            v = compress(i)
            dic = {}
            flag = True
            for j in range(len(pl)):
                if pl[j] in "0123456789" or v[j] in "0123456789":
                    if pl[j] != v[j]:
                        flag = False
                        break
                else:
                    if pl[j] in dic:
                        if dic[pl[j]] != v[j]:
                            flag = False
                            break
                    else:
                        dic[pl[j]] = v[j]
                        
            if flag:
                res.append(i) 
        return res
        