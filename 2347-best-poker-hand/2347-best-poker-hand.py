class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        else:
            if len(set(ranks)) == 5:
                return "High Card"
            dic = {}
            for i in ranks:
                if i in dic.keys():
                    dic[i] += 1
                else:
                    dic[i] = 1
            m = 0
            print(dic)
            for i in dic:
                m = max(m,dic[i])
            if m > 2:
                return "Three of a Kind"
            if m == 2:
                return "Pair"
            if m == 1:
                return "High Card"
                
                
        