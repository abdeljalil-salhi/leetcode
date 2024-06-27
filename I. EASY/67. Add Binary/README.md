# 67. Add Binary

[View problem on LeetCode](https://leetcode.com/problems/add-binary/)

![Submission](image.png)

We will first convert the binary string to a decimal using int() function in python. The int() function in Python and Python3 converts a number in the given base to decimal. Then we will add it and then again convert it into a binary number using bin() function.

```
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"


Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
```
