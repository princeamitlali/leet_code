class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dic = {"type":0,"color":1,"name":2}
        ruleKey = dic[ruleKey]
        res = 0
        for item in items:
            if item[ruleKey] == ruleValue:
                res += 1
        return res
                
        