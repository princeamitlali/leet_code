import copy
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        char_list = []
        words.sort(key = lambda x:len(x))
        for i in licensePlate:
            if i.isalpha():
                i = i.lower()
                char_list.append(i)
        for word in words:
            char_list_copy = copy.deepcopy(char_list)
            for i in word:
                if i.isalpha():
                    i = i.lower()
                    if i in char_list_copy:
                        char_list_copy.remove(i)
                    if len(char_list_copy) == 0:
                        return word

        return ""