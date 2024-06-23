# 9. Palindrome Number

[View problem on LeetCode](https://leetcode.com/problems/palindrome-number/)

Respecting the follow-up condition, I didn't convert the integer to a string. Instead, I reversed the integer and compared it with the original integer. If they are equal, then the integer is a palindrome.

Time complexity: $O(\log x)$

Space complexity: $O(1)$

```
Given an integer x, return true if x is a palindrome, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.


Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-2^31 <= x <= 2^31 - 1


Follow up: Could you solve it without converting the integer to a string?
```
