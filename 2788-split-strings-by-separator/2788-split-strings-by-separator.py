class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        s = ""
        for i in words:
            s +=separator
            s +=i
        s = s[1:].split(separator)
        temp = []
        for i in s:
            if i != "":
                temp.append(i)
        return temp
        