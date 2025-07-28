class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx = {}
        ans = 0
        start = 0
        for i in range(len(s)):
            if char_idx.get(s[i],None) != None:
                start = max(char_idx[s[i]] + 1, start)
            char_idx[s[i]] = i
            ans = max(ans, i - start + 1)
        return ans