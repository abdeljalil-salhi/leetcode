# 1109. Corporate Flight Bookings

[View problem on leetcode](https://leetcode.com/problems/corporate-flight-bookings/)

![Submission](image.png)

At first, I followed a naive approach to solve this problem. I created a list of size `n` and initialized all elements to 0. Then, I iterated over the bookings and updated the elements in the list accordingly. Finally, I returned the list. This approach gave me a TLE, it was expected because the time complexity of this approach is $O(n*m)$ where $n$ is the number of flights and $m$ is the number of bookings.

```python
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer, b = [0] * n, len(bookings)
        for i in range(b):
            for j in range(bookings[i][0] - 1, bookings[i][1]):
                answer[j] += bookings[i][2]
        return answer
```

So how can I try to optimize this solution to only have a time complexity of $O(n+m)$?

Well, I realized that I don't need to update all the elements in the list. I only need to update the first element of the booking and the last element of the booking. So, I can iterate over the bookings and update the first element of the booking by adding the number of seats to it and update the last element of the booking by subtracting the number of seats from it. This way, I can update the list in $O(m)$ time. Finally, I can iterate over the list and calculate the prefix sum to get the final answer.

```python
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * n

        # Process the bookings
        for start, end, seats in bookings:
            answer[start - 1] += seats
            if end < n:
                answer[end] -= seats

        # Calculate the prefix sum
        for i in range(1, n):
            answer[i] += answer[i - 1]

        return answer
```

Time complexity of my solution is $O(n+m)$.

Space complexity of my solution is $O(1)$ because I am not using any extra space other than the input and output.

```

There are n flights that are labeled from 1 to n.

You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
Explanation:
Flight labels: 1 2 3 4 5
Booking 1 reserved: 10 10
Booking 2 reserved: 20 20
Booking 3 reserved: 25 25 25 25
Total seats: 10 55 45 25 25
Hence, answer = [10,55,45,25,25]
Example 2:

Input: bookings = [[1,2,10],[2,2,15]], n = 2
Output: [10,25]
Explanation:
Flight labels: 1 2
Booking 1 reserved: 10 10
Booking 2 reserved: 15
Total seats: 10 25
Hence, answer = [10,25]

Constraints:

1 <= n <= 2 _ 10^4
1 <= bookings.length <= 2 _ 10^4
bookings[i].length == 3
1 <= firsti <= lasti <= n
1 <= seatsi <= 10^4

```

```

```
