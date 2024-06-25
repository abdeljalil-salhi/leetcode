# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If we reach a leaf node, return None to stop the recursive calls
        if not root:
            return root

        # Swap the left and right children of the current node
        swap = root.left
        root.left = root.right
        root.right = swap

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Only the root node will arrive here after all the recursive calls
        return root
