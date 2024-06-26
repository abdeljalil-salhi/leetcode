# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # If the root is None or the root is one of the nodes, return the root to stop the recursion
        if not root or root == p or root == q:
            return root

        # Recursively search for the nodes in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If the nodes are found in both the left and right subtrees, the current root is the LCA
        if left and right:
            return root

        # If the nodes are found in only one of the subtrees, return the node found
        return left if left else right
