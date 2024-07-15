# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashmap = {}
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in hashmap:
                hashmap[parent] = TreeNode(parent)
            if child not in hashmap:
                hashmap[child] = TreeNode(child)
            if isLeft:
                hashmap[parent].left = hashmap[child]
            else:
                hashmap[parent].right = hashmap[child]
            children.add(child)

        for parent, _, _ in descriptions:
            if parent not in children:
                return hashmap[parent]

        return None
