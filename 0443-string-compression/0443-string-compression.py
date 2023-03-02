class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("_")
        prev = ""
        count = 0
        res = []
        for i in chars:
            # print(i)
            if prev != i:
                if count > 0:
                    for j in str(count+1):
                        res.append(str(j))
                
                res.append(i)
                count = 0
                prev = i
            else:
                count += 1
            # print(res)
        for i in range(len(res)):
            chars[i] = res[i]
        # chars = res.copy()
        return len(res)-1
        