class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # The idea is to generate all the subsets of the given list
        # and calculate the XOR of each subset
        def backtrack(start: int, xor: int) -> None:
            nonlocal ans
            ans += xor
            for i in range(start, n):
                backtrack(i + 1, xor ^ nums[i])

        ans, n = 0, len(nums)
        backtrack(0, 0)  # Start from the first element with XOR 0 recursively

        return ans
