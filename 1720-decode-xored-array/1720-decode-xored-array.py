class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        prev = first
        for i in range(len(encoded)):
            t = encoded[i]
            encoded[i] = encoded[i] ^ prev
            prev = encoded[i]
        encoded.insert(0,first)
        return encoded
        
        