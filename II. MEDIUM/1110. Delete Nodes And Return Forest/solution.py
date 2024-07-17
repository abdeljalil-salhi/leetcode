# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        subtrees = []

        def dfs(node: Optional[TreeNode], is_new_root: bool) -> Optional[TreeNode]:
            if not node:
                return None

            parent_deleted = node.val in to_delete_set
            if is_new_root and not parent_deleted:
                subtrees.append(node)

            node.left = dfs(node.left, parent_deleted)
            node.right = dfs(node.right, parent_deleted)

            return None if parent_deleted else node

        dfs(root, True)

        return subtrees
