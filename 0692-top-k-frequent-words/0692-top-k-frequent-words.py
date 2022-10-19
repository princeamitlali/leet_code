from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]: 
        c = Counter
        words_dict = c(sorted(words))
        words_dict = sorted(words_dict.items() , key = lambda items:items[1],reverse=True)
        val=[]
        for i in range(k):
            val.append(words_dict[i][0])
        return val
                
            
        