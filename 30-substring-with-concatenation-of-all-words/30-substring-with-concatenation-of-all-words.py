class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        s_length, words_length = len(s), len(words)
        each_word_length = len(words[0])
        words_counter = collections.Counter(words)
        start_indexes = []
        for i in range(s_length-(words_length*each_word_length)+1):
            words_seen = collections.defaultdict(int)
            for j in range(words_length):
                cur_word_index = i+j*each_word_length
                cur_word = s[cur_word_index:cur_word_index+each_word_length]
                if cur_word not in words_counter:
                    break

                words_seen[cur_word] += 1
                if words_seen[cur_word] > words_counter[cur_word]:
                    break

                if j+1 == words_length:
                    start_indexes.append(i)

        return start_indexes