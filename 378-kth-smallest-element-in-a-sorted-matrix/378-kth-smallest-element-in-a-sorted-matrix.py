import numpy as np
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(np.array(matrix).flatten())[k-1]