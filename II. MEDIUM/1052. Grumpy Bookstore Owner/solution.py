class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n, maximum, already = (
            len(customers),
            0,
            sum(c if not grumpy[i] else 0 for i, c in enumerate(customers)),
        )

        # Fixed size sliding window
        for i in range(n - minutes + 1):
            current = already
            for j in range(minutes):
                current += customers[i + j] if grumpy[i + j] else 0
            maximum = max(maximum, current)

        return maximum
