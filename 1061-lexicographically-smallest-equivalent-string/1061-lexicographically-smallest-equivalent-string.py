class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
        
        def find(char):
            if char != d[char]:
                d[char] = find(d[char])
            return d[char]
        
        def update(char, value):
            if char != d[char]:
                update(d[char], value)
            d[char] = value
            
        for a,b in zip(s1, s2):
            p,q = find(a), find(b)
            
            if p > q:
                update(p, q)
            else:
                update(q, p)

        return "".join([find(d[i]) for i in baseStr])
        