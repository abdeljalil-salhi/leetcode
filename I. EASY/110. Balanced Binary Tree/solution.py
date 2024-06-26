# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool | int:
        if not root:
            return True

        left = self.isBalanced(root.left)
        if not left:
            return 0

        right = self.isBalanced(root.right)
        if not right:
            return 0

        if abs(left - right) > 1:
            return False
        return max(left, right) + 1
