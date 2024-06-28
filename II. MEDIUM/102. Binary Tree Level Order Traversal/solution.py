# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Initialize a deque to store the nodes and a list to store the answer
        deq, ans, n = deque([(root, 0)]), [], 0

        # Breadth-first search the tree
        while deq:
            node, level = deq.popleft()

            # If the level is greater than the length of the answer list, append a new list
            if level == n:
                ans.append([])
                n += 1

            # Append the value of the node to the answer list
            ans[level].append(node.val)

            # Add the children of the node to the deque
            if node.left:
                deq.append((node.left, level + 1))
            if node.right:
                deq.append((node.right, level + 1))

        return ans
