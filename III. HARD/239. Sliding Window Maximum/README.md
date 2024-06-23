# 239. Sliding Window Maximum

[View problem on LeetCode](https://leetcode.com/problems/sliding-window-maximum/submissions/1297707002/)

![Submission](image.png)

This problem is a classic example of using the sliding window technique to find the maximum value in each window of size `k`. The key idea is to use a deque (double-ended queue) to store the indices of elements in the current window in a way that the values of these elements are in decreasing order. This allows us to quickly find the maximum value in the window.

Why overcomplicating things and use a deque and all you would say ? Well, this is a simple code that solves this hard problem in 4 lines; but good luck submitting it to LeetCode, it will just exceed the time limit when tested with crazy large test cases.

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window, n = [], len(nums)
        for i in range(n - k + 1):
            window.append(max(nums[i:i+k]))
        return window
```

```
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
```

## Explanation of the Code written by ChatGPT:

Handling the Special Case:
If `k == 1`, each window is just a single element, so the result is the original array.

Initialization:

- `window`: A list to store the maximum values for each window.
- `n`: The length of the input array `nums`.
- `deq`: A deque to store the indices of elements in the current window in a way that the values of these elements are in decreasing order.
- `l` and `r`: Pointers for the left and right ends of the sliding window, both initialized to 0.

Sliding Window:

- The outer `while` loop runs until the right pointer `r` reaches the end of the array.

Maintaining the Deque:

- The `while` loop inside the main loop ensures the deque contains indices of elements in decreasing order of their values in `nums`. If the current element `nums[r]` is greater than the element at the last index in the deque, the last index is removed from the deque.
- The current index `r` is appended to the deque.

Removing Out-of-Window Elements:

- If the left pointer `l` is greater than the index at the front of the deque, it means the element at that index is out of the current window, so it is removed from the deque.

Recording the Maximum Value:

- Once the window size reaches `k` (i.e., `r + 1 >= k`), the element at the front of the deque (which is the maximum in the current window) is appended to the result list `window`.
- The left pointer `l` is then incremented to shrink the window size, preparing for the next iteration.

Incrementing the Right Pointer:

- The right pointer `r` is incremented to expand the window size.

Return Result:

- The function returns the list `window`, which contains the maximum values for each sliding window of size `k`.

This code efficiently computes the maximum value in each sliding window of size `k` with a time complexity of $O(n)$.
