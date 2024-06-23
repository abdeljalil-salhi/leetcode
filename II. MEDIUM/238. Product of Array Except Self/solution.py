class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the answer array with 1s.
        answer = [1] * n

        # First pass: Calculate the running product of the prefixes.
        product = 1
        for i in range(n):
            answer[i] = product
            product *= nums[i]

        # Second pass: Calculate the running product of the suffixes.
        product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= product
            product *= nums[i]

        # The answer is the product of the prefixes and suffixes.
        return answer
