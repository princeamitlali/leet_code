class Solution:
    def minDeletions(self, s: str) -> int:
        freq = sorted(Counter(s).values(), reverse=True)
        
        dele = 0
        unused_freq = len(s)
        for f in freq:
            unused_freq = min(unused_freq, f)
            dele += f - unused_freq

            if unused_freq > 0:
                unused_freq -= 1

        return dele
        
        