# 995. Minimum Number of K Consecutive Bit Flips

[View problem on leetcode](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/)

![Submission](image.png)

Well, at first I just tried to use a normal sliding window approach to solve this problem. But I was getting TLE for large test cases. So I had to find a way to optimize this solution that runs in $O(n . k)$:

```python
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n, c = len(nums), 0

        for i in range(n - k + 1):
            flip = False
            for j in range(k):
                if (not nums[i + j] and not j) or flip:
                    flip = True
                    nums[i + j] = 0 if nums[i + j] else 1
            if flip:
                c += 1

        for i in range(n):
            if not nums[i]:
                return -1

        return c
```

So, I optimized my solution by using a greedy approach. I used a deque to keep track of the indices where flips start. This new solution runs in $O(n)$, check it out in the [solution.py](solution.py) file.

Time complexity: $O(n)$

Space complexity: $O(k)$ for the deque

```
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].


Example 2:

Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].


Example 3:

Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation:
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]


Constraints:

1 <= nums.length <= 10^5
1 <= k <= nums.length
```

## Explanation of the Code written by ChatGPT:

### Initialization:

- `n`: The length of the input array `nums`.
- `deq`: A deque to keep track of the indices where flips start.
- `c`: A counter to keep track of the total number of flips.
- `l`: A variable to keep track of the current number of flips, just so we don't have to count them every time using the `len` function; which would be $O(k)$ each time.

### Iterating Through the Array:

- Loop through each element in the array `nums` using index `i`:
  - **Removing Out-of-Window Elements**:
    - If the deque is not empty and the first element in the deque is out of the current window (i.e., `deq[0] <= i - k`), remove it from the deque and decrement `l`.
  - **Determining the Current Bit Value**:
    - If the number of flips `l` is even, the current bit remains as in `nums[i]`.
    - If `l` is odd, the current bit is the opposite of `nums[i]` (i.e., `1 - nums[i]`).
  - **Flipping the Current Window**:
    - If the current bit value is `0`, a flip is required:
      - If the remaining window size from `i` is less than `k` (i.e., `i + k > n`), it's impossible to flip, return `-1`.
      - Add the current index `i` to the deque, increment both `l` and `c` by 1.

### Return Result:

- The variable `c` contains the total number of K-bit flips required to make all elements of `nums` equal to 1.
- If the loop completes without returning `-1`, return the total number of flips `c`.
