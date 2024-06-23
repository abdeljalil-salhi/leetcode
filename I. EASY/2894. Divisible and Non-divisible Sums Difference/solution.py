class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = sum(i if i % m else 0 for i in range(1, n + 1))
        num2 = sum(i if not i % m else 0 for i in range(1, n + 1))
        return num1 - num2
