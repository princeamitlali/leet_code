

from itertools import permutations
import math
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num = n
        l = len(str(num))
        dict = {1:[0,3],2:[4,6],3:[7,9],4:[10,13],5:[14,16],6:[17,19],7:[20,23],8:[24,26],9:[27,29],10:[30,33],11:[34,34]}

        val = dict[l]
        for i  in range(val[0],val[1]+1):
            if int("".join(sorted(str(pow(2,i))))) == int("".join(sorted(str(num)))):
                return True

        return False
