"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        # Mapping: original node -> cloned node
        visited = {node: Node(node.val)}
        # Double-ended queue for BFS
        deq = deque([node])

        while deq:
            # Pop the leftmost node that needs processing
            _node = deq.popleft()
            # Clone the neighbors of the node if they are not visited yet
            for neighbor in _node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    deq.append(neighbor)
                # Append the cloned neighbor to the cloned node
                visited[_node].neighbors.append(visited[neighbor])

        # Return the clone of the first node reference
        return visited[node]
