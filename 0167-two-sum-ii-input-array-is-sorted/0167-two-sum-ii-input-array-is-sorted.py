class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = sorted(list(set(numbers)))
        for i in n:
            if (target - i) in numbers:
                first = numbers.index(i)+1
                second = first + numbers[first:].index(target-i) +1
                return [first, second]
        