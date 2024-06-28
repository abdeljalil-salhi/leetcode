# 973. K Closest Points to Origin

[View problem on LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/)

![Submission](image.png)

The solution is to sort the points based on their distance from the origin and return the first k points. The distance of a point from the origin is calculated as $\sqrt{x^2 + y^2}$.

So my thoughts/solutions upgraded as follows:

1. I first misunderstood the problem (I thought the points would be unique, so I used a hashmap to store the distances and points):

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hmap = {}
        for point in points:
            hmap[tuple(point)] = sqrt(
                pow(abs(point[0] - 0), 2) + pow(abs(point[1] - 0), 2)
            )
        hmap = sorted(hmap, key=hmap.get)
        return hmap[:k]
```

2. Then I realized that the points are not unique, so I changed my approach to store the points as a tuple with their distance in an array, and sort them based on the distance:

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = [(point[0] ** 2 + point[1] ** 2, point) for point in points]
        arr = sorted(arr, key=lambda x: x[0])
        return [point for _, point in arr[:k]]
```

3. I realized that I could do the same directly to the points without creating a new list:

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]
```

Time Complexity: $O(n \log k)$

Space Complexity: $O(1)$

```

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:

1 <= k <= points.length <= 10^4
-10^4 <= xi, yi <= 10^4

```

```

```
