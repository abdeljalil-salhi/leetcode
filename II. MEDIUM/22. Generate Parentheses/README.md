# 22. Generate Parentheses

[View problem on LeetCode](https://leetcode.com/problems/generate-parentheses/)

![Submission](image.png)

I used a recursive backtracking approach to solve this problem. I created a backtracking function that takes in the current string, the number of open parentheses, and the number of close parentheses.

The base case is when the length of the current string is equal to the total number of parentheses multiplied by 2. In this case, I add the current string to the result list.

If the number of open parentheses is less than the total number of parentheses, I call the backtracking function recursively with an open parenthesis added to the current string.

If the number of close parentheses is less than the number of open parentheses, I call the backtracking function recursively with a close parenthesis added to the current string.

Time complexity is $O(4^n/sqrt(n))$, where $n$ is the number of pairs of parentheses.

```
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
```
