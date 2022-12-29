class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0
        for sentence in sentences:
            m = max(m,len(sentence.split(" ")))
        return m
        