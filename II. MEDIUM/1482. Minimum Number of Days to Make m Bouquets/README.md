# 1482. Minimum Number of Days to Make m Bouquets

[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)

![Submission](image.png)

Time complexity is $O(n \log(\text{max(bloomDay) - \text{min(bloomDay)}}))$ where $n$ is the length of the `bloomDay` list.

```
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.



Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.


Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.


Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.


Constraints:

bloomDay.length == n
1 <= n <= 10^5
1 <= bloomDay[i] <= 10^9
1 <= m <= 10^6
1 <= k <= n
```

## Explanation of the Code written by ChatGPT:

### Helper Function `able`:

- This function checks if it is possible to make `m` bouquets by day `days`.
  - `bouquets`: Counter for the number of bouquets made.
  - `flowers`: Counter for the consecutive flowers.
- Iterate through each `day` in `bloomDay`:
  - If `days` is greater than or equal to `day`, increment the `flowers` counter.
  - If `flowers` reaches `k`, reset `flowers` to 0 and increment `bouquets`.
  - If `bouquets` reaches `m`, return `True` (it is possible to make the required bouquets by this day).
  - If `days` is less than `day`, reset `flowers` to 0 (since the current flower hasn't bloomed by `days`).
- Return `False` if the number of `bouquets` is less than `m` after iterating through the `bloomDay`.

### Initial Check:

- Calculate `n` as the length of `bloomDay`.
- If `m * k` is greater than `n`, it's impossible to make the required bouquets with the available flowers, so return `-1`.

### Binary Search for Minimum Days:

- Initialize `low` to the minimum value in `bloomDay` and `high` to the maximum value in `bloomDay`.
- Perform a binary search:
  - Calculate `mid` as the average of `low` and `high`.
  - Use the `able` function to check if it is possible to make `m` bouquets by `mid` days.
  - If `able(mid)` returns `True`, update `high` to `mid` (narrow the search to smaller days).
  - If `able(mid)` returns `False`, update `low` to `mid + 1` (narrow the search to larger days).

### Return Result:

- After the binary search completes, `low` will be the minimum number of days required to make `m` bouquets. Return `low` as the final result.
