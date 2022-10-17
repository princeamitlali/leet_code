class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        li = [ 0 for i in range(26)]
        print(len(li))
        for i in sentence:
            val = ord(i) - 97
            li[val] = 1
        if 0 in li:
            return False
        return True
        