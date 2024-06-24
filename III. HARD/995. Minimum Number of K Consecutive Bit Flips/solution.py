class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n, deq, c, l = len(nums), deque(), 0, 0

        for i in range(n):
            # Remove the first element if it is out of the window
            if deq and deq[0] <= i - k:
                deq.popleft()
                l -= 1

            # If the number of flips is even, the current number is the same as the original number
            if l % 2 == 0:
                current = nums[i]
            # If the number of flips is odd, the current number is the opposite of the original number
            # So we need to get the opposite number of the current number
            else:
                current = 1 - nums[i]

            # If the current number is 0, we need to flip the current window
            if current == 0:
                # If the current window is out of the range, we can't flip the window
                if i + k > n:
                    return -1

                # Add the index of the current window to the deque and increase the number of flips
                deq.append(i)
                l += 1
                c += 1

        return c
