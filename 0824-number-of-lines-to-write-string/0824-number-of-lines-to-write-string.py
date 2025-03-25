class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        rem_width = 100
        line = 0
        for i in s:
            width = widths[ord(i)-97]
            if width > rem_width:
                line += 1
                rem_width = 100
           
            rem_width -= width
            print(rem_width)
        return line + 1 , 100 - rem_width
        