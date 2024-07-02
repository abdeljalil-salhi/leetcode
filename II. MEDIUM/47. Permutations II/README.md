# 47. Permutations II

[View problem on LeetCode](https://leetcode.com/problems/permutations-ii/)

![Submission](image.png)

I used the same approach as in the previous problem [46. Permutation](/II.%20MEDIUM/46.%20Permutations/), but added the used numbers to a set to avoid duplicates.

Time complexity is $O(n!)$ since we have to generate all possible permutations.

```
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]


Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
```
