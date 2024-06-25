class Solution:
    def __init__(self):
        self.original = -1
        self.m = -1
        self.n = -1
        self.visited = set()

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # If this is the first call, set the original color and image dimensions
        if self.original == -1:
            self.original = image[sr][sc]
            self.m = len(image)
            self.n = len(image[0])

            # If the original color is the same as the new color, return the image as is
            if self.original == color:
                return image

        # If the current pixel is within the image boundaries, has the original color, and has not been visited
        if (
            0 <= sr < self.m
            and 0 <= sc < self.n
            and image[sr][sc] == self.original
            and (sr, sc) not in self.visited
        ):
            image[sr][sc] = color
            self.visited.add((sr, sc))
            
            # Recursively call the function on the neighboring pixels
            self.floodFill(image, sr + 1, sc, color)
            self.floodFill(image, sr - 1, sc, color)
            self.floodFill(image, sr, sc + 1, color)
            self.floodFill(image, sr, sc - 1, color)

        return image
