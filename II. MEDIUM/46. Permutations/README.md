# 46. Permutations

[View problem on LeetCode](https://leetcode.com/problems/permutations/)

![Submission](image.png)

I used a normal backtracking algorithm to solve this problem.

I used a helper function to recursively generate all the permutations. The helper function takes the current index as argument.

If the current index is equal to the length of the input array, it means we have generated a permutation. We add the permutation to the result list and return.

Otherwise, we iterate over the array and swap the current index with the current element. We then call the helper function recursively with the current index incremented by 1. After the recursive call, we swap the current index with the current element back to the original state.

Time complexity is $O(n!)$ where $n$ is the length of the input array. This is because we generate all the permutations.

```
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]


Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
```
