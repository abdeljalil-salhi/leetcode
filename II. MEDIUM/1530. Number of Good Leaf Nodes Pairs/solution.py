# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        pairs = 0

        def dfs(node: TreeNode) -> List[int]:
            if not node:
                return []
            if not node.left and not node.right:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal pairs

            for dist1 in left:
                for dist2 in right:
                    if dist1 + dist2 <= distance:
                        pairs += 1

            return [distance + 1 for distance in (left + right)]

        dfs(root)

        return pairs
