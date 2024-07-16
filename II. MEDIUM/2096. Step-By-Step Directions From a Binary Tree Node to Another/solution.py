# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def dfs(node: TreeNode, path: str, target: int) -> str:
            if not node:
                return ""

            if node.val == target:
                return path

            path.append("L")
            res = dfs(node.left, path, target)
            if res:
                return res
            path.pop()

            path.append("R")
            res = dfs(node.right, path, target)
            if res:
                return res
            path.pop()

            return ""

        startPath = dfs(root, [], startValue)
        destPath = dfs(root, [], destValue)

        i, ns, nd = 0, len(startPath), len(destPath)
        while i < min(ns, nd) and startPath[i] == destPath[i]:
            i += 1

        return "".join(["U"] * (ns - i) + destPath[i:])
