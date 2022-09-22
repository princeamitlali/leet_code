class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split(" ")
        #print(words_list)
        s = ""
        for i in words_list:
            s = s+ i[::-1] + " "
        return s[:-1]