class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        max_deque, min_deque = deque(), deque()
        left = longest = 0

        for right in range(n):
            # Keep the decreasing order of max_deque
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Keep the increasing order of min_deque
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # If the difference between the maximum and minimum values in the window is greater than limit
            # then we need to shrink the window
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # If the maximum element is out of the window, then remove it
                if max_deque[0] < left:
                    max_deque.popleft()
                # Same for the minimum element
                if min_deque[0] < left:
                    min_deque.popleft()

            # Keep track of the longest window
            longest = max(longest, right - left + 1)

        return longest
