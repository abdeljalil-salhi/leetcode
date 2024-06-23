# 633. Sum of Square Numbers

[View problem on LeetCode](https://leetcode.com/problems/sum-of-square-numbers/)

![Submission](image.png)

It took me a bit of research to understand the math behind this problem and provide an efficient-among-all solution. I used Fermat's theorem on sums of two squares to solve this problem. The theorem states that a non-negative integer `c` can be expressed as the sum of two squares if and only if the prime factorization of `c` contains no prime congruent to 3 modulo 4 raised to an odd power.

Time complexity is $O(\sqrt{c})$ _(I believe)_.

```
Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.



Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5


Example 2:

Input: c = 3
Output: false


Constraints:

0 <= c <= 2^31 - 1
```
