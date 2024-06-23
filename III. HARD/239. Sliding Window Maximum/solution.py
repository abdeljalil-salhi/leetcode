class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # If the window size is 1, then return the input list
        if k == 1:
            return nums

        window, n, deq = [], len(nums), deque()
        left = right = 0

        while right < n:
            # Keep the decreasing order of the deque
            while deq and nums[deq[-1]] < nums[right]:
                deq.pop()
            deq.append(right)

            # If the maximum element is out of the window, then remove it
            if left > deq[0]:
                deq.popleft()

            # In the beginning, we need to fill the window with k elements
            # After that, we can append the maximum element to the window
            if right + 1 >= k:
                window.append(nums[deq[0]])
                left += 1

            right += 1

        return window
