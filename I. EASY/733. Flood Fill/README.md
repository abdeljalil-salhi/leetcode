# 733. Flood Fill

[View problem on LeetCode](https://leetcode.com/problems/flood-fill/)

![Submission](image.png)

## Intuition

The flood fill problem is analogous to the "bucket fill" tool in paint programs. When a user selects a pixel and a color, the tool changes the color of the selected pixel and all connected pixels with the same initial color. This can be effectively solved using depth-first search (DFS) to explore all connected pixels.

## Approach

1. **Initialization**: Use an `__init__` method to set up instance variables that will store the original color of the starting pixel, the dimensions of the image, and a set to keep track of visited pixels.
2. **Base Case Handling**: If the starting pixel's color is already the target color, return the image immediately to avoid unnecessary operations.
3. **Recursive Flood Fill**: Implement the flood fill using DFS:
   - Check if the current pixel is within bounds, has the original color, and has not been visited.
   - Change the color of the current pixel.
   - Mark the current pixel as visited.
   - Recursively call the flood fill function for the four adjacent pixels (up, down, left, right).

## Complexity

- Time complexity: $O(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns in the image. In the worst case, each pixel is visited once.

- Space complexity: $O(m \times n)$ due to the recursion stack and the visited set. In the worst case, the recursion stack could hold $O(m \times n)$ calls if the entire image needs to be filled.

```
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.



Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.


Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.


Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 2^16
0 <= sr < m
0 <= sc < n
```

## Example 1 Visualization

![Example 1](image-1.png)
