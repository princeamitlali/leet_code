class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(" ")
        print(text)
        res = 0
        for i in text:
            for j in brokenLetters:
                if j in i:
                    res += 1
                    break
        
        
        
        return len(text) - res
        