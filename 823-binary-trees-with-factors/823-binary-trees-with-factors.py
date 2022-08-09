class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        nums = set(arr)
        n = len(arr)
        num_to_products = defaultdict(list)
        max_val = arr[-1]
        for i in range(n):
            for j in range(i, n):
                key = arr[i] * arr[j]
                # time optimization
                if key > max_val:
                    break
                # space optimization
                if key in nums:
                    num_to_products[key].append((arr[i], arr[j]))
                
                
        result = n
        num_to_nb_of_trees = dict()
        for num in arr:
            factors = num_to_products[num]
            amount_of_combos = 0
            for i, j in factors:
                new_combos = 0
                new_combos += 1
                new_combos += num_to_nb_of_trees[i]
                new_combos += num_to_nb_of_trees[j]
                new_combos += num_to_nb_of_trees[i] * num_to_nb_of_trees[j]
                if i != j:
                    new_combos *= 2
                amount_of_combos += new_combos
            num_to_nb_of_trees[num] = amount_of_combos
            result += amount_of_combos
        return result % (10**9 + 7)