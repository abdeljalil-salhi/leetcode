# 110. Balanced Binary Tree

[View problem on LeetCode](https://leetcode.com/problems/balanced-binary-tree/)

![Submission](image.png)

I used a tricky way to solve this problem. I changed the return type of the function to either be an integer or a boolean. The function returns an integer to calculate the height of the subtree without the usage of a helper function. The function is called recursively; only the very first call returns a boolean value meaning the tree is balanced or not. This way my function will serve two purposes. It will calculate the height of the subtree and also check if the tree is balanced or not for the leetcode test cases.

```
Given a binary tree, determine if it is height-balanced.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true


Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false


Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
```
