# 330. Patching Array

[View problem on LeetCode](https://leetcode.com/problems/patching-array/)

![Submission](image.png)

Time complexity is $O(\log n)$ where $n$ is the length of the `nums` list.

Space complexity is $O(1)$.

```
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.



Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.


Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 10^4
nums is sorted in ascending order.
1 <= n <= 2^31 - 1
```

## Explanation of the Code written by ChatGPT:

### Problem Understanding:

The goal is to find the minimum number of patches required to make the numbers from 1 to `n` using the numbers in the `nums` list (which is sorted in ascending order).

### Initialization:

- `patches`: A counter to keep track of the number of patches added.
- `i`: An index to iterate through the `nums` list.
- `current_range`: A variable that represents the maximum number we can currently achieve using the numbers in `nums` and the patches added.
- `l`: The length of the `nums` list.

### Iterative Process:

- Iterate while `current_range` is less than or equal to `n` (the target range we want to cover):
  - If `i` is within bounds and `nums[i]` is less than or equal to `current_range`:
    - Extend `current_range` by adding `nums[i]` to it.
    - Increment `i` to move to the next number in `nums`.
  - If `i` is out of bounds or `nums[i]` is greater than `current_range`:
    - Add `current_range` itself to `current_range` (essentially, patching the number `current_range` to extend the range).
    - Increment the `patches` counter because we had to patch the range to cover `current_range`.

### Return Result:

- After exiting the loop, `patches` will contain the minimum number of patches required to cover all numbers from 1 to `n` using `nums`. Return `patches` as the final result.
