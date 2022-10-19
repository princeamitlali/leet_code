from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        new_words = sorted(words)
        words_dict = []
        count = 0
        # for i in range(len(new_words)-1):
        #     if new_words[i] == new_words[i+1]:
        #         count = count + 1
        #     else:
        #         words_dict.append([new_words[i],count])
        #         count = 0
        # words_dict.append([new_words[len(new_words)-1],count])   
        c = Counter
        words_dict = c(new_words)
        words_dict = sorted(words_dict.items() , key = lambda items:items[1],reverse=True)
        val=[]
        for i in range(k):
            val.append(words_dict[i][0])
        return val
                
            
        