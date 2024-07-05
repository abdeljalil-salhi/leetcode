class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        n = len(word)

        def dfs(i: int, j: int, p: int, visited: Set[Tuple[int, int]]) -> bool:
            if p == n:
                return True
            if (
                i >= ROWS
                or i < 0
                or j >= COLS
                or j < 0
                or (i, j) in visited
                or board[i][j] != word[p]
            ):
                return False

            visited.add((i, j))

            found = (
                dfs(i + 1, j, p + 1, visited)
                or dfs(i - 1, j, p + 1, visited)
                or dfs(i, j + 1, p + 1, visited)
                or dfs(i, j - 1, p + 1, visited)
            )

            visited.remove((i, j))

            return found

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0] and dfs(i, j, 0, set()):
                    return True

        return False
