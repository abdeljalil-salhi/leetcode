class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n, max_xor = len(nums), 0

        for i in range(n):
            for j in range(i + 1, n):
                # If the current pair is a strong pair
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    # Calculate the XOR of the current pair
                    current_xor = nums[i] ^ nums[j]
                    # Update the maximum XOR if the current XOR is greater
                    if current_xor > max_xor:
                        max_xor = current_xor

        return max_xor
