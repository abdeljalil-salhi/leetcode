# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calculateHeight(root)
        return self.diameter

    def calculateHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        lh = self.calculateHeight(node.left)
        rh = self.calculateHeight(node.right)

        self.diameter = max(self.diameter, lh + rh)

        return max(lh, rh) + 1
