class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_list = sorted(score, reverse = True)
        temp = []
        for i in score:
            val = sorted_list.index(i)
            if val == 0:
                temp.append("Gold Medal")
            elif val == 1:
                temp.append("Silver Medal")
            elif val == 2:
                temp.append("Bronze Medal")
            else:
                temp.append(str(val + 1))
        return temp
        