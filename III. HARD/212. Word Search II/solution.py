class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = ""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        result, root = set(), TrieNode()

        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word

        def dfs(i: int, j: int, node: TrieNode, visited: Set[Tuple[int, int]]) -> None:
            if (
                i >= ROWS
                or i < 0
                or j >= COLS
                or j < 0
                or (i, j) in visited
                or board[i][j] not in node.children
            ):
                return

            visited.add((i, j))
            node = node.children[board[i][j]]
            if node.word:
                result.add(node.word)

            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i + di, j + dj, node, visited)

            visited.remove((i, j))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] in root.children:
                    dfs(i, j, root, set())

        return result
