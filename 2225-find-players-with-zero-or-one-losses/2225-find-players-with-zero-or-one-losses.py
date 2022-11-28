class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set(chain(*matches))                
        loses = Counter([y for _,y in matches])    

        zeros = sorted(players - set(loses))  
        ones  = sorted(filter(lambda x: loses[x]==1, players)) 

        return [zeros, ones]
       
        