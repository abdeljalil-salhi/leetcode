# 21. Merge Two Sorted Lists

[View problem on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)

![Submission](image.png)

Time complexity is $O(n)$ where $n$ is the length of the longest list.

```
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


Example 2:

Input: list1 = [], list2 = []
Output: []


Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
```

## Example 1 Visualization

![Example 1](image-1.png)
