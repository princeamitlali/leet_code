class Solution:
    def finalString(self, s: str) -> str:
        tem = ""
        for i in s:
            if i == 'i':
                tem = tem[::-1]
            else:
                tem += i
                
        return tem