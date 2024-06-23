class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = water = 0

        while left < right:

            # If the height of the left wall is less than the height of the right wall
            # and the height of the left wall is greater than the left_max
            # then update the left_max to the height of the left wall.
            # Otherwise, add the difference between the left_max and the height of the left wall to the water.
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1

            # If the height of the right wall is less than the height of the left wall
            # and the height of the right wall is greater than the right_max
            # then update the right_max to the height of the right wall.
            # Otherwise, add the difference between the right_max and the height of the right wall to the water.
            elif height[right] <= height[left]:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        # Return the total amount of water trapped between the walls.
        return water
