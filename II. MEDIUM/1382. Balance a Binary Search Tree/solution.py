# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes, n = [], 0

        def storeBST(root: TreeNode) -> None:
            if not root:
                return None

            nonlocal n

            storeBST(root.left)

            nodes.append(root)
            n += 1

            storeBST(root.right)

        def buildTree(start: int, end: int) -> TreeNode:
            if start > end:
                return None

            mid = (start + end) // 2
            node = nodes[mid]

            node.left = buildTree(start, mid - 1)
            node.right = buildTree(mid + 1, end)

            return node

        storeBST(root)

        return buildTree(0, n - 1)
