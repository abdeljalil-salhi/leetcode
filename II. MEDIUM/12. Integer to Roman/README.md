# 12. Integer to Roman

[View problem on LeetCode](https://leetcode.com/problems/integer-to-roman/)

![Submission](image.png)

Time complexity is $O(1)$ since the length of the `romans` and `integers` lists is fixed (13 elements).

```
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.



Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places


Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII


Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV


Constraints:

1 <= num <= 3999
```

## Explanation of the Code written by ChatGPT:

### Problem Understanding:

The goal is to convert an integer to its corresponding Roman numeral representation.

### Initialization:

- `romans`: A list of Roman numeral symbols, ordered from smallest to largest with special cases included.
- `integers`: A list of integer values corresponding to the Roman numeral symbols in `romans`.
- `n`: Initialize to 12, which is the index of the last element in the `integers` and `romans` lists.
- `ans`: An empty string to accumulate the resulting Roman numeral representation.

### Conversion Process:

- Use a `while` loop to process the integer `num` until it is reduced to 0.
  - Calculate `value` as the integer division of `num` by `integers[n]`. This determines how many times the current Roman numeral can be used.
  - Update `num` using the modulo operation to get the remainder after accounting for the current Roman numeral.
  - Use another `while` loop to append the current Roman numeral `romans[n]` to `ans`, `value` times.
  - Decrement `n` to move to the next largest Roman numeral.

### Return Result:

- After the loop completes, `ans` contains the Roman numeral representation of the input integer `num`. Return `ans` as the final result.
