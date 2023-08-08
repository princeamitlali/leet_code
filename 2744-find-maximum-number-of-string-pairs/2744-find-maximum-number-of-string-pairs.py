class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        dic = {}
        count = 0
        for i in words:
            dic[i] = dic.get(i[::-1],0) + 1
            if dic[i] >1:
                count += 1
                
        return count
        
        